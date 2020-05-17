try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin

from flask import request, redirect, url_for, current_app, flash
import os
import uuid

import PIL
from PIL import Image
from itsdangerous import BadSignature, SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from newsdph.settings import Operations
import time

def generate_token(user):
    expiration = current_app.config['LOGIN_LIFETIME']
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    token = s.dumps({'id': user.id}).decode('ascii')
    return token, expiration


def validate_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except (BadSignature, SignatureExpired):
        return False
    user = User.query.get(data['id'])
    if user is None:
        return False
    # g.current_user = user
    return True


def get_token():
    # Flask/Werkzeug do not recognize any authentication types
    # other than Basic or Digest, so here we parse the header by hand.
    if 'Authorization' in request.headers:
        try:
            token_type, token = request.headers['Authorization'].split(None, 1)
        except ValueError:
            # The Authorization header is either empty or has no token
            token_type = token = None
    else:
        token_type = token = None
    return token_type, token


def clean_login_token():
    token, token_type = get_token()
    if token:
        # payload = validate_token()
        user = True
        if not user:
            result = (None, "User authentication failed, user does not exist")
        else:
            # todo update database jwt_login_time
            result = (True, "")
    else:
        result = (None, "No user authentication token provided")
    return result


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token_type, token = get_token()

        # Flask normally handles OPTIONS requests on its own, but in the
        # case it is configured to forward those to the application, we
        # need to ignore authentication headers and let the request through
        # to avoid unwanted interactions with CORS.
        if request.method != 'OPTIONS':
            if token_type is None or token_type.lower() != 'bearer':
                return api_abort(400, 'The token type must be bearer.')
            if token is None:
                return token_missing()
            if not validate_token(token):
                return invalid_token()
        return f(*args, **kwargs)

    return decorated


# def validate_token(user, token, operation, new_password=None):
#     s = Serializer(current_app.config['SECRET_KEY'])
#     try:
#         data = s.loads(token)
#     except (SignatureExpired, BadSignature):
#         return False
#
#     if operation != data.get('operation') or user.id != data.get('id'):
#         return False
#
#     if operation == Operations.CONFIRM:
#         user.confirmed = True
#     elif operation == Operations.RESET_PASSWORD:
#         user.set_password(new_password)
#     elif operation == Operations.CHANGE_EMAIL:
#         new_email = data.get('new_email')
#         if new_email is None:
#             return False
#         if User.query.filter_by(email=new_email).first() is not None:
#             return False
#         user.email = new_email
#     else:
#         return False
#
#     db.session.commit()
#     return True
