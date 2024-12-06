from flask import Blueprint, request, jsonify
from app.database import get_collection
from app.auth.jwt_required import jwt_required

bp = Blueprint('csv', __name__)

@bp.route('/get-csv', methods=['POST'])
@jwt_required
def get_csv():
    data = request.get_json()

    email = request.email
    file_name = data['file_name']

    collection = get_collection('csv_data')

    document = collection.find_one({'email': email, 'file_name': file_name}, {'file_name': 1, 'data': 1})

    if not document:
        return jsonify({"error": "File not found for the provided email"}), 404

    return jsonify({'file_name': document['file_name'], 'data': document['data']})
