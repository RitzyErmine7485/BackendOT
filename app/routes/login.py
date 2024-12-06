from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from app.database import get_collection

bp = Blueprint('login', __name__)

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Validate input
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password are required"}), 400
    
    username = data["username"]
    password = data["password"]

    # Find user in MongoDB
    try:
        collection = get_collection("users")
        
        # Check if the user exists
        user = collection.find_one({"username": username})
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Verify password
        if not check_password_hash(user["password"], password):
            return jsonify({"error": "Invalid password"}), 401
        
        return jsonify({"message": "Login successful"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
