from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from app.database import get_collection

bp = Blueprint('signup', __name__)

@bp.route('/signup', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get("email") or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password are required"}), 400
    
    email = data["email"]
    username = data["username"]
    password = data["password"]
    
    hashed_password = generate_password_hash(password)

    try:
        collection = get_collection("users")
        
        if collection.find_one({"email": email}):
            return jsonify({"error": "Email already exists"}), 400

        user_data = {
            "email": email,
            "username": username,
            "password": hashed_password,
            "imageUri": "https://media.istockphoto.com/id/610003972/vector/vector-businessman-black-silhouette-isolated.jpg?s=612x612&w=0&k=20&c=Iu6j0zFZBkswfq8VLVW8XmTLLxTLM63bfvI6uXdkacM=",
        }
        
        collection.insert_one(user_data)
        
        return jsonify({"message": "User created successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
