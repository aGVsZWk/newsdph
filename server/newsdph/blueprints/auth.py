from newsdph.models import User
from flask import render_template, flash, redirect, url_for, Blueprint, jsonify, request
from flask_login import login_user, logout_user, login_required, current_user, login_fresh, confirm_login
from newsdph.extensions import db
from newsdph.settings import Operations
from newsdph.utils.token import generate_token, validate_token
from newsdph.utils.response import make_response
from newsdph.utils.uid import get_capta

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')   # todo 改成form
    password = request.json.get('password')
    remember = request.json.get('remember')
    print(email, password, remember)
    user = User(email)
    data = {
        "id": None,
        "token": None
    }
    t1 = user.validate_password(password)
    t2= login_user(user, remember=remember)
    print(t1, t2)
    if t1 and t2:
        data["id"]=user.data.get("id")
        data["token"] = generate_token(data["id"], operation="login").decode()

        return make_response(data, status=1)
    return make_response(data=data, status=0)


@app.route('/verify')
def verify():
    email = request.data.get('email')
    code = get_capta(length=12)
    
    return make_response('', 1)


@app.route('/register', methods=['POST'])
def register():
    pass
    return render_template('expression')
