from flask import Blueprint, request
from flaskr.view.welcome_viewer import welcome_viewer

welcome_blueprint = Blueprint("welcome", __name__)

@welcome_blueprint.route("/welcome")
def delphi_control():
    return welcome_viewer()