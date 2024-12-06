from flask import jsonify

def handle_errors(e):
    return jsonify({"error": str(e)}), 500
