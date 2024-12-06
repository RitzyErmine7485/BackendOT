import jwt
import datetime
from app.config import Config

SECRET_KEY = Config.SECRET_KEY

def generate_jwt(user):
    """Generate JWT token for a given user."""
    expiration_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    payload = {
        'email': user['email'],
        'exp': expiration_time
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def decode_jwt(token):
    """Decode JWT token and extract the user."""
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded['user']
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")
