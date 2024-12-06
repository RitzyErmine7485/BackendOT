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
        
        user = collection.find_one({"email": email})
        
        if not user:
            return jsonify({"message": "User not found"}), 404

        csv_data_collection = get_collection("csv_data")
        data = list(csv_data_collection.find({"uploaded_by": email}, {"_id": 0}))
        
        if not data:
            return jsonify([{"message": "No data yet"}]), 200
        
        return jsonify(data), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
