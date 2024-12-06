from flask import Blueprint, request, jsonify
from app.database import get_collection
from app.auth.jwt_required import jwt_required

bp = Blueprint('profile', __name__)

@bp.route('/profile', methods=['GET'])
@jwt_required
def get_data():
    email = request.email

    try:
        collection = get_collection("users")
        
        user = collection.find_one({"email": email}, {"_id": 0, "username": 1, "email": 1, "imageUri": 1})
        
        if not user:
            return jsonify({"message": "No data found for this profile"}), 404
        
        user["imageUri"] = user.get("imageUri", "https://media.istockphoto.com/id/610003972/vector/vector-businessman-black-silhouette-isolated.jpg?s=612x612&w=0&k=20&c=Iu6j0zFZBkswfq8VLVW8XmTLLxTLM63bfvI6uXdkacM=")
        
        return jsonify(user), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
