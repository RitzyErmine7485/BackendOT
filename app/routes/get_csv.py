from flask import Blueprint, request, jsonify
from app.database import get_collection
from app.auth.jwt_required import jwt_required

bp = Blueprint('csv', __name__)

@bp.route('/get-csv', methods=['POST'])
@jwt_required
def get_csv():
    data = request.get_json()

    file_name = data['file_name']

    collection = get_collection('csv_data')

    document = collection.find_one({'file_name': file_name}, {'file_name': 1, 'data': 1})

    if not document:
        return jsonify({"error": "File not found"}), 404

    return jsonify({'file_name': document['file_name'], 'data': document['data']})
