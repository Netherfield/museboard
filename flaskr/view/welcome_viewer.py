from flask import render_template

def welcome_viewer():
    """
    return "welcome.html" template
    :return:
    """
    return render_template("welcome.html")