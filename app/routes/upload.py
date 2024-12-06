from flask import Blueprint, request, jsonify
import pandas as pd
import io
from app.database import get_collection

bp = Blueprint('upload', __name__)

@bp.route('/upload', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    if not file.filename.endswith('.csv'):
        return jsonify({"error": "File must be a CSV"}), 400

    try:
        df = pd.read_csv(io.StringIO(file.stream.read().decode("UTF-8")))
        data_json = df.to_dict(orient='records')
        collection = get_collection("csv_data")

        file_metadata = {
            "file_name": file.filename,
            "data": data_json
        }

        collection.insert_one(file_metadata)
        return jsonify({"message": "Data uploaded successfully", "file_name": file.filename}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
