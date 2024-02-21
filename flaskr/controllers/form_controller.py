from flask import Blueprint, request, redirect, url_for, render_template
from view.form_viewer import form_viewer
from database.connection_manager import sqlite_connector, PATH_SQL

form_blueprint = Blueprint("form", __name__)


@form_blueprint.route("/form", methods=['GET', 'POST'])
def form_control():
    """
    If 'POST' add form arguments in a list and create a board with data
    else 'GET' render template '__FORM__.html'
    :return:
    """
    if request.method == "POST":
        # Adding form data in a list
        request_list = [request.form.get("nick"), request.form.get("country"), request.form.get("age"),
                        request.form.get("topic1"), request.form.get("topic2")]
        conx, cursor = sqlite_connector(PATH_SQL)
        my_data = list()
        for x in request_list:
            # doing query for each item and save in 'my_data'
            QUERY = f"SELECT * FROM items WHERE Description LIKE '%{x}%' AND Img_Link != '' LIMIT 3"
            cursor.execute(QUERY)
            res = cursor.fetchall()
            my_data += res
        QUERY_ins = """INSERT INTO board (Item_Name, Img_Link, Description, Description_Url, Short_Description, Item_Type)
        VALUES (?, ?, ?, ?, ?, ?);"""
        cursor.execute("DELETE FROM board") # Delete existing Board 'items'
        for x in my_data:
            # adding data to 'board'
            cursor.execute(QUERY_ins, x[1:]) # skip 'ID'
        conx.commit()
        conx.close()
        # redirect to 'Home'
        return redirect(url_for("home.home_control"))
    # render '__FORM__.html'
    return render_template("__FORM__.html")
