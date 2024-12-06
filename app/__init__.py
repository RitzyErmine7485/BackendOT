from flask import Flask
from flask_cors import CORS
from .routes import get_data, upload
from .middleware.error_handler import handle_errors
from .database import init_db

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Initialize database
    init_db(app)

    # Register middleware
    app.register_error_handler(Exception, handle_errors)

    # Register routes
    app.register_blueprint(upload.bp)
    app.register_blueprint(get_data.bp)

    return app
