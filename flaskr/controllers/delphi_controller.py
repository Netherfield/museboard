from flask import Blueprint, request
from flaskr.view.delphi_viewer import delphi_viewer

delphi_blueprint = Blueprint("delphi", __name__)

@delphi_blueprint.route("/")
def delphi_control():
    return delphi_viewer()