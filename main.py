from flask import Flask
from controller.accident_controller import accident_blueprint

def create_flask_app():
    app = Flask(__name__)
    app.register_blueprint(accident_blueprint, url_prefix="/api")
    return app


if __name__ == '__main__':
    app = create_flask_app()
    app.run(debug=True)