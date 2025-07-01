from flask import Flask
from .routes.youtube import youtube_bp
from .routes.instagram import instagram_bp
from .routes.linkedin import linkedin_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(youtube_bp)
    app.register_blueprint(instagram_bp)
    app.register_blueprint(linkedin_bp)
    return app
