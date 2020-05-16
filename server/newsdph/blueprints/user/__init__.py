from flask import Blueprint, jsonify, request, current_app

user_bp = Blueprint('user', __name__)
from .api.online import *
