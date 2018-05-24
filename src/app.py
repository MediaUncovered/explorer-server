from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/query/<string:word>')
    def query(word):
        pass

    return app
