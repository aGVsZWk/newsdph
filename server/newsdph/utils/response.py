from flask import jsonify

def make_response(data, status=1, code=200, message=("nice!", "s")):
    if data and isinstance(data, dict):
        payload = {
            "status": status,
            **data
        }
    if not isinstance(message, tuple) or len(message) != 2:
        return jsonify({})
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
        "msg": message[0],
        "msg_type": message[1],
        "payload": payload
    }
    return jsonify(ret)
