from flask import render_template

def form_viewer():
    """
    Return '__FORM__.html' template
    :return:
    """
    return render_template("form.html")
