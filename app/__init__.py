from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from .models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) or None


from app import views