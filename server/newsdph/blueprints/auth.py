from flask import render_template, flash, redirect, url_for, Blueprint, jsonify, request
from flask_login import login_user, logout_user, login_required, current_user, login_fresh, confirm_login
from newsdph.extensions import db
from newsdph.settings import Operations
from newsdph.utils import generate_token, validate_token, redirect_back
from newsdph.responseutils import make_response
auth_bp = Blueprint('auth', __name__)
from models import User


@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.data.get('email')
    user = User(email)
    return make_response(user.data)
