from flask import Blueprint, request, jsonify
from app.database import get_collection
from app.auth.jwt_required import jwt_required

bp = Blueprint('data', __name__)

@bp.route('/get-data', methods=['GET'])
@jwt_required  # Ensure the user is authenticated
def get_data():
    username = request.username
    
    try:
        collection = get_collection("csv_data")
        
        data = list(collection.find({"uploaded_by": username}, {"_id": 0}))
        
        if not data:
            return jsonify({"message": "No data found for this user"}), 404
        
        return jsonify(data), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
