from flask import Blueprint, request, jsonify
from app.database import get_collection
from app.auth.jwt_required import jwt_required
from bson.objectid import ObjectId

bp = Blueprint('delete_user', __name__)

@bp.route('/delete-user', methods=['DELETE'])
@jwt_required
def delete_user():
    try:
        email = request.email
        
        users_collection = get_collection('users')
        
        result = users_collection.delete_one({'email': email})
        
        if result.deleted_count == 0:
            return jsonify({"message": "User not found"}), 404
        
        return jsonify({"message": "User successfully deleted"}), 200
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"message": "An error occurred while deleting the user"}), 500
