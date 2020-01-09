from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '6cc755bc60a328138498a6c010532565'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///mydictionary.db'
db = SQLAlchemy(app)

from backend import routes

#TODO: add system of user login,
# flash cards,
# option to choice vocabulary of translate or mean