from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    # import views
    from app.views import userView, postView
    app.register_blueprint(userView.bp)
    app.register_blueprint(postView.bp)

    return app
