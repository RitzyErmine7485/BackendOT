from flask import Flask
from flask_cors import CORS
from .routes import upload_routes, data_routes
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
    app.register_blueprint(upload_routes.bp)
    app.register_blueprint(data_routes.bp)

    return app
