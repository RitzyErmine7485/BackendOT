import jwt
import datetime
from flask import current_app

# Secret key for JWT encoding and decoding (should be kept secret in production)
SECRET_KEY = current_app.config['SECRET_KEY']

def generate_jwt(username):
    """Generate JWT token for a given username."""
    expiration_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    payload = {
        'username': username,
        'exp': expiration_time
    }
    
    # Create JWT token
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def decode_jwt(token):
    """Decode JWT token and extract the username."""
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded['username']
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")
