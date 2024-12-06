from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from app.database import get_collection

bp = Blueprint('signup', __name__)

@bp.route('/signup', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password are required"}), 400
    
    username = data["username"]
    password = data["password"]
    
    hashed_password = generate_password_hash(password)

    try:
        collection = get_collection("users")
        
        if collection.find_one({"username": username}):
            return jsonify({"error": "Username already exists"}), 400

        user_data = {
            "username": username,
            "password": hashed_password
        }
        
        collection.insert_one(user_data)
        
        return jsonify({"message": "User created successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
