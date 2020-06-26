from flask import Blueprint

bp = Blueprint('fleet', __name__)

from app.fleet import routes
