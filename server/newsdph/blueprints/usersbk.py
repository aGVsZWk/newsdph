import flask
from flask import jsonify, request
from newsdph.utils import Pagination

users_bp = flask.Blueprint(
    'users',
    __name__,
    url_prefix='/api'
)


@users_bp.route('/users/all', methods=["GET", "POST"])
def get_all_users():

    users = [
        {"id": 1, "name": "张三", "gender": "男", "age": "18", "address": "地球", "classId": "1"},
        {"id": 2, "name": "李四", "gender": "男", "age": "19", "address": "地球", "classId": "1"},
        {"id": 3, "name": "王五", "gender": "男", "age": "18", "address": "地球", "classId": "1"},
        {"id": 4, "name": "张三", "gender": "男", "age": "22", "address": "地球", "classId": "1"},
        {"id": 5, "name": "张三", "gender": "男", "age": "18", "address": "地球", "classId": "1"},
        {"id": 6, "name": "张三", "gender": "男", "age": "18", "address": "地球", "classId": "1"},
        {"id": 7, "name": "张三", "gender": "男", "age": "18", "address": "地球", "classId": "1"},
        {"id": 8, "name": "张三", "gender": "男", "age": "18", "address": "地球", "classId": "2"},
        {"id": 9, "name": "张三", "gender": "男", "age": "18", "address": "地球", "classId": "2"},
        {"id": 10, "name": "张三", "gender": "男", "age": "19", "address": "地球", "classId": "2"},
        {"id": 11, "name": "张三", "gender": "女", "age": "18", "address": "地球", "classId": "2"},
        {"id": 12, "name": "张三", "gender": "女", "age": "18", "address": "地球", "classId": "2"},
        {"id": 13, "name": "张三", "gender": "女", "age": "18", "address": "地球", "classId": "2"},
        {"id": 14, "name": "张三", "gender": "女", "age": "18", "address": "地球", "classId": "2"}
    ]
    # current = request.args.get('current', None) or request.json.get('current', None)
    # pageSize = request.args.get('pageSize', None) or request.json.get('pageSize', None)
    if request.method == "GET":
        current = request.args.get('current', None)
        pageSize = request.args.get('pageSize', None)
    else:
        current = request.json.get('current', None)
        pageSize = request.json.get('pageSize', None)

    classId = request.args.get("classId")
    name = request.args.get("name")
    if classId:
        users = list(filter(lambda x: x["classId"]==classId, users))
    if name:
        users = list(filter(lambda x: x["name"] == name, users))

    pagination = Pagination(current, pageSize, len(users))

    data = {
        "state": 200,
        "data": users[pagination.start: pagination.end],
        "pagination": {
            "current": pagination.current,
            "pageSize": pagination.pageSize,
            "total": len(users),
            "totalPages": pagination.pageCount,
        }
    }

    return jsonify(data)
