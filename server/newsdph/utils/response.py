from flask import jsonify

def make_response(data, code=200, message=("nice!", "s")):
    if code >= 200 and code < 300:
        status = 1
    else:
        status = 0
    if data and isinstance(data, dict):
        payload = {
            "status": status,
            **data
        }
    if not isinstance(message, tuple) or len(message) != 2:
        return jsonify({
            "code": 500,
            "msg": "msg error",
            "msg_type": "e",
            "payload":{"status":0}
        })
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
