from flask import request, jsonify
from app.utils.jwt_utils import decode_jwt

def jwt_required(f):
    """Decorator to protect routes requiring JWT authentication."""
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({"error": "Token is missing"}), 403

        try:
            token = token.replace('Bearer ', '')
            email = decode_jwt(token)
            request.email = email 
        except Exception as e:
            return jsonify({"error": str(e)}), 403
        
        return f(*args, **kwargs)

    return decorator
