from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from app.database import get_collection
from app.utils.jwt_utils import generate_jwt

bp = Blueprint('login', __name__)

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password are required"}), 400
    
    username = data["username"]
    password = data["password"]

    try:
        collection = get_collection("users")
        
        user = collection.find_one({"username": username})
        if not user:
            return jsonify({"error": "User not found"}), 404

        if not check_password_hash(user["password"], password):
            return jsonify({"error": "Invalid password"}), 401
        
        token = generate_jwt(username)
        
        return jsonify({"message": "Login successful", "token": token}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
