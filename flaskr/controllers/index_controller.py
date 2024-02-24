from flask import Blueprint
from flaskr.view.index_viewer import index_viewer

index_blueprint = Blueprint("index", __name__)

@index_blueprint.route("/")
def index_control():
    return index_viewer()