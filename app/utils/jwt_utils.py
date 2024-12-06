import jwt
import datetime
from app.config import Config

SECRET_KEY = Config.SECRET_KEY

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
