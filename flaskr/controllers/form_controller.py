from flask import Blueprint, request, redirect, url_for, render_template
from flaskr.view.form_viewer import form_viewer
from flaskr.database.connection_manager import sqlite_connector, PATH_SQL

form_blueprint = Blueprint("form", __name__)


@form_blueprint.route("/form", methods=['GET', 'POST'])
def form_control():
    """
    If 'POST' add form arguments in a list and create a board with data
    else 'GET' render template '__FORM__.html'
    :return:
    """
    try:
        if request.method == "POST":
            conx, cursor = sqlite_connector(PATH_SQL)
            # Adding form data in a list
            request_list = [request.form.get("user"), request.form.get("country"),
                            request.form.get("topic1"), request.form.get("topic2")]
            print(request_list)
            my_data = list()
            for x in request_list:
                # doing query for each item and save in 'my_data'
                QUERY = f"SELECT * FROM items WHERE Description LIKE '%{x}%' LIMIT 3"
                cursor.execute(QUERY)
                res = cursor.fetchall()
                if res:
                    for x in res:
                        my_data.append(x[1:])
            cursor.execute("DELETE FROM board")
            conx.commit()
            QUERY_ins = """INSERT INTO board (Item_Name, Img_Link, Description, Description_Url, Short_Description, Item_Type)
            VALUES (?, ?, ?, ?, ?, ?)"""
            cursor.executemany(QUERY_ins, my_data)
            conx.commit()
            conx.close()
            return redirect(url_for("home.home_control", tag="", path=""))
    except Exception as e:
        print(f"An error occurred: {e}")
    # render '__FORM__.html'
    return render_template("form.html")
