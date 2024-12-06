from flask import Blueprint, request, jsonify
from app.database import get_collection
from app.auth.jwt_required import jwt_required

bp = Blueprint('edit_profile', __name__)

@bp.route('/edit-profile', methods=['PUT'])
@jwt_required
def edit_profile():
    email = request.email
    data = request.get_json()

    try:
        collection = get_collection("users")
        
        user = collection.find_one({"email": email})
        if not user:
            return jsonify({"message": "User not found"}), 404
        
        updated_data = {}
        if 'username' in data:
            updated_data['username'] = data['username']
        if 'imageUri' in data:
            updated_data['imageUri'] = data['imageUri']
        
        if updated_data:
            collection.update_one({"email": email}, {"$set": updated_data})

        return jsonify({"message": "Profile updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
