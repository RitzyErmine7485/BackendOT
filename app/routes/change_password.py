from flask import Blueprint, request, jsonify
from app.database import get_collection
from app.auth.jwt_required import jwt_required
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('change-password', __name__)

@bp.route('/change-password', methods=['POST'])
@jwt_required
def change_password():
    email = request.email
    data = request.get_json()

    old_password = data.get('old_password')
    new_password = data.get('new_password')

    if not old_password or not new_password:
        return jsonify({"message": "Old password and new password are required"}), 400

    try:
        collection = get_collection("users")
        
        user = collection.find_one({"email": email})
        if not user:
            return jsonify({"message": "User not found"}), 404
        
        if not check_password_hash(user['password'], old_password):
            return jsonify({"message": "Incorrect password"}), 401

        if len(new_password) < 8:
            return jsonify({"message": "New password must be at least 8 characters long"}), 400

        hashed_new_password = generate_password_hash(new_password)

        collection.update_one({"email": email}, {"$set": {"password": hashed_new_password}})

        return jsonify({"message": "Password changed successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
