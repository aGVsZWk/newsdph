from flask import request, make_response
from . import resource_bp


# 上传文件列表
@resource_bp.route('/uploadFiles', methods=['POST'])
def uploadFileList():
    print("hahahah")
    files = request.files
    print(files)
    return make_response({"nice": "nice"}, 200, "完美")


@resource_bp.route('/heartBeat')
def heartBeat():
    # print("你麻痹")
    print('nice')
    return make_response({"nice": "nice"}, 200, "完美")
