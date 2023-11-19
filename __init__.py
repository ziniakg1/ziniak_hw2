from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import environ
import os

load_dotenv('.flaskenv')

DB_NAME = enviorn.get('DATABASE')
basedir = os.path.abspath(ps.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

DB_CONFIG_STR = 'sqlite:////' + os.path.join(basedir,DB_NAME)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONFIG_STR
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

from app import routes,models