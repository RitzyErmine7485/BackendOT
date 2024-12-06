from flask import Flask
from flask_cors import CORS
from .routes import get_data, upload, login
from .middleware.error_handler import handle_errors
from .database import init_db

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    init_db(app)

    app.register_error_handler(Exception, handle_errors)

    app.register_blueprint(upload.bp)
    app.register_blueprint(get_data.bp)
    app.register_blueprint(login.bp)

    return app
