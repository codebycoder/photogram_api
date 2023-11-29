from user.models import User
from datetime import datetime, timedelta
import jwt
from decouple import config

jwt_secret_key = config('JWT_SECRET_KEY')
jwt_algorithm = config('JWT_ALGORITHM')


def generate_token(user: User):
    """Generate token for user"""

    expires_at = datetime.utcnow() + timedelta(days=config('JWT_EXPIRY_TIME'))
    payload = {
        'user_id': user.id,
        'username': user.username,
        'email': user.email,
        'is_admin': user.is_admin,
        'exp': expires_at
    }
    token = jwt.encode(payload, key=jwt_secret_key,
                       algorithm=jwt_algorithm)
    return {
        'user': user,
        'access_token': token,
        'token_type': 'Bearer',
        'expires_at': expires_at.timestamp()
    }


def verify_access_token(access_token: str):
    """
    verifies access token and returns user id, username, email
    """

    try:
        payload = jwt.decode(
            jwt=access_token, key=jwt_secret_key, algorithms=jwt_algorithm)
    except jwt.ExpiredSignatureError:
        raise Exception('Token expired')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token')

    user_id = payload.get('user_id')
    username = payload.get('username')
    email = payload.get('email')
    is_admin = payload.get('is_admin')
    return user_id, username, email, is_admin
