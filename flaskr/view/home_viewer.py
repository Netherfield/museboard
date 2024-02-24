from flask import render_template, session

def home_viewer(data:list):
    """
    Return '__HOME__.html' template with 'data' input
    :param data:
    :return:
    """
    return render_template("home.html", data=data)

