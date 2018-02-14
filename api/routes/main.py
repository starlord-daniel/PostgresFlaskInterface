from api import api
from flask import Blueprint, make_response, request, jsonify
from flask.views import MethodView

simple = Blueprint('simple', __name__)

import json
import sympy

@simple.route('/')
@simple.route('/hello')
def hello():
    """Renders a sample page."""
    return "Hello World!"