from flask import Blueprint

resource_bp = Blueprint('resource', __name__)

from .api import *   # noqa
