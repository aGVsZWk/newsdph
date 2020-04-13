import uuid
import string
import random

def get_uuid():
    return str(uuid.uuid1()).replace("-", "")



def get_capta(length=6):
    capta = ''
    chars = ''.join([string.ascii_letters, string.digits])
    for i in range(length):
        capta += random.choice(chars)
    return capta
