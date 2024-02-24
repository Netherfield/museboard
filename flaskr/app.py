from flask import Flask, jsonify, render_template
from flaskr.controllers.home_controller import home_blueprint
from flaskr.controllers.form_controller import form_blueprint
from flaskr.controllers.index_controller import index_blueprint
from flaskr.controllers.mydata_api import board_blueprint

apx = Flask(__name__)

apx.register_blueprint(home_blueprint)
apx.register_blueprint(form_blueprint)
apx.register_blueprint(index_blueprint)
apx.register_blueprint(board_blueprint)

apx.secret_key = "MUSEBOARD"


if __name__ == "__main__":
    apx.run(debug=True)