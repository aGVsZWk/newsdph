import uuid
import string
import random
from newsdph.extensions import redis_client


def get_uuid():
    return str(uuid.uuid1()).replace("-", "")

def get_capta(length=6):
    capta = ''
    chars = ''.join([string.ascii_letters, string.digits])
    for i in range(length):
        capta += random.choice(chars)
    return capta

def verify_capta(code, email="", tel_number=""):
    """
    验证email或message验证码
    :param code: 验证码
    :param code:
    :return:
    """
    r = False
    if not code:
        return r
    _code = None
    if email:
        _code = redis_client.get(email)
    if tel_number:
        _code = redis_client.get(tel_number)
    if _code and _code.decode().lower() == code:
        r = True
    # return r
    return True

def set_capta(code, key):
    r = redis_client.setex(key, current_app.config['VERIFY_CODE_LIFETIME'], code)
    return True if r else False
