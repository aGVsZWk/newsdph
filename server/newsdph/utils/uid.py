import uuid


def get_uuid():
    return str(uuid.uuid1()).replace("-", "")
