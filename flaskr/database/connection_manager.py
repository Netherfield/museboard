from flaskr.database.sqlite_config import *


def sqlite_connector(PATH:str) -> (sqlite3.Connection, sqlite3.Cursor):
    """
    return connector and cursor of 'PATH'
    :param PATH:
    :return:
    """
    conx = sqlite3.connect(PATH)
    cursor = conx.cursor()

    return conx, cursor

