from accounts.models import CustomUser
import jwt 
from django.conf import settings
from datetime import datetime, timedelta

def generate_access_token(user):
    created_payload = {
        'user_id': user.username,
        'iat': datetime.now(),
        'exp': datetime.now() + timedelta(minutes=15),
        'type': 'access'
    }
    token = jwt.encode(created_payload, settings.SECRET_KEY_JWT, algorithm='HS256')

    return token


def generate_refresh_token(user):
    created_payload = {
        'user_id': user.username,
        'iat': datetime.now(),
        'exp': datetime.now() + timedelta(days=15),
        'type': 'refresh'
    }

    token = jwt.encode(created_payload, settings.SECRET_KEY_JWT, algorithm='HS256')