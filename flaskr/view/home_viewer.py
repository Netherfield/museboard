from flask import render_template, session

def home_viewer(data:list):
    """
    Return '__HOME__.html' template with 'data' input
    :param data:
    :return:
    """
    session["data_form"] = data[0]
    print(session)
    return render_template("__HOME__.html", data=data)

