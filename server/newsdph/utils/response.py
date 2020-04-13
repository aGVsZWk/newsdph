from flask import jsonify

def make_response(data, status=1, code=200):
    if data and isinstance(data, dict):
        payload = {
            "status": status,
            **data
        }
    elif data and isinstance(data, list):
        payload = {
            "data": data,
            "status": status
        }
    else:
        payload = {
            "status": status
        }
    ret = {
        "code": code,
        "msg": "nice!!!",
        "payload": payload
    }
    return jsonify(ret)
