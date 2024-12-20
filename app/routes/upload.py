from flask import Blueprint, request, jsonify
import pandas as pd
import io
from app.database import get_collection
from app.auth.jwt_required import jwt_required
from datetime import datetime

bp = Blueprint('upload', __name__)

@bp.route('/upload', methods=['POST'])
@jwt_required
def upload_csv():
    email = request.email
    
    file = list(request.files.values())[0]
    
    if not file.filename.endswith('.csv'):
        return jsonify({"error": "File must be a CSV"}), 400
    
    try:
        df = pd.read_csv(io.StringIO(file.stream.read().decode("UTF-8")))
        data_json = df.to_dict(orient='records')
        upload_date = datetime.now().isoformat()

        file_metadata = {
            "file_name": file.filename,
            "uploaded_by": email,
            "upload_date": upload_date,
            "data": data_json
        }

        collection = get_collection("csv_data")
        collection.insert_one(file_metadata)
        
        return jsonify({"message": "Data uploaded successfully", "file_name": file.filename}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
