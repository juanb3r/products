from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://juanber:Juan123..@localhost/vallenatearte'

db = SQLAlchemy(app)

from app import routes
