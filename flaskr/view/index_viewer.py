from flask import render_template

def index_viewer():
    """
    return 'index' template
    :return:
    """
    return render_template("index.html")