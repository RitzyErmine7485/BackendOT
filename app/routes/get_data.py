from flask import Blueprint, jsonify
from app.database import get_collection

bp = Blueprint('data', __name__)

@bp.route('/get-data', methods=['GET'])
def get_data():
    try:
        collection = get_collection("csv_data")
        data = list(collection.find({}, {"_id": 0}))
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
