from flask import jsonify

def make_response(data, code=200, status=1):
    payload = {
        "data": data,
        "status": status
    }
    ret = {
        "code": code,
        "msg": "nice!!!",
        "payload": payload
    }
    return jsonify(ret)
