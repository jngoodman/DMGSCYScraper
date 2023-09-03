from flask import Flask

app = Flask(__name__)


class FlaskApp:

    @app.route("/")
    def hello_world(self):
        return "<p>Hello World</p>"
