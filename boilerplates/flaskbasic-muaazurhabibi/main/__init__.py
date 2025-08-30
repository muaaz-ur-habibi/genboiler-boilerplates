from flask import Flask

def BUILD():
    app = Flask(__name__)
    app.secret_key = "secret key" # change this

    from .routes import routes
    app.register_blueprint(routes)

    return app