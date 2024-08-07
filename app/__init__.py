from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///password_manager.db'
    app.config['SECRET_KEY'] = 'Mimi070424'
    
    db.init_app(app)
    
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app