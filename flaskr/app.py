from flask import Flask
from flaskr.controllers.home_controller import home_blueprint
from flaskr.controllers.form_controller import form_blueprint
from flaskr.controllers.index_controller import index_blueprint
from flaskr.controllers.mydata_api import board_blueprint
from flaskr.controllers.delphi_controller import delphi_blueprint
from flaskr.controllers.welcome_controller import welcome_blueprint
from flaskr.controllers.color_api import color_blueprint

apx = Flask(__name__)

apx.register_blueprint(home_blueprint)
apx.register_blueprint(form_blueprint)
apx.register_blueprint(index_blueprint)
apx.register_blueprint(board_blueprint)
apx.register_blueprint(delphi_blueprint)
apx.register_blueprint(welcome_blueprint)
apx.register_blueprint(color_blueprint)

apx.secret_key = "MUSEBOARD"


if __name__ == "__main__":
    apx.run(debug=True)