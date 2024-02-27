from flask import Blueprint, request
from flaskr.view.home_viewer import home_viewer
from flaskr.database.connection_manager import sqlite_connector, PATH_SQL

home_blueprint = Blueprint("home", __name__)

def get_branch():
    """
    SELECT FROM table first 4 branch
    :return:
    """
    pass

@home_blueprint.route("/home", methods= ["GET", "POST"])
def home_control():
    """
    return 'home_viewr' function from view and pass 'res' as argument
    :return:
    """
    # res = get_branch()
    current_url = request.url
    print("home", current_url)
    res = [[1, ["topic1", "topic2", "topic3","topic4"]], [2, ["topic5","topic6","topic7","topic8"]],
           [3, ["topic9", "topic10", "topic11","topic12"]], [4, ["topic13","topic14","topic15","topic16"]]]
    return home_viewer(res)

