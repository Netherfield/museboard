from flask import Blueprint
from view.home_viewer import home_viewer
from database.connection_manager import sqlite_connector, PATH_SQL

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/home", methods= ["GET", "POST"])
def home_control():
    """
    return 'home_viewr' function from view and pass 'res' as argument
    :return:
    """
    conx, cursor = sqlite_connector(PATH_SQL)
    cursor.execute("SELECT * FROM board") # here for board request management
    res = cursor.fetchall()
    conx.commit()
    conx.close()
    return home_viewer(res)
