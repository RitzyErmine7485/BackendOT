from flask import Blueprint, request, jsonify
from app.database import get_collection
from app.auth.jwt_required import jwt_required

bp = Blueprint('data', __name__)

@bp.route('/get-data', methods=['GET'])
@jwt_required
def get_data():
    email = request.email

    try:
        collection = get_collection("users")
        
        user = collection.find_one({"email": email}, {"_id": 0, "username": 1})
        
        if not user:
            return jsonify({"message": "User not found"}), 404

        username = user["username"]

        csv_data_collection = get_collection("csv_data")
        data = list(csv_data_collection.find({"uploaded_by": username}, {"_id": 0}))
        
        if not data:
            return jsonify({"message": "No data found for this user"}), 404
        
        return jsonify(data), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
