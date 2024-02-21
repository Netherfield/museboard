from flask import Flask
from controllers.home_controller import home_blueprint
from controllers.form_controller import form_blueprint

apx = Flask(__name__)

apx.register_blueprint(home_blueprint)
apx.register_blueprint(form_blueprint)
apx.secret_key = "MUSEBOARD"

if __name__ == "__main__":
    apx.run(debug=True)