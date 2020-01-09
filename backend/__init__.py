from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend import user_password_external

app = Flask(__name__)
app.config['SECRET_KEY'] = user_password_external.APPKEY
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///mydictionary.db'
db = SQLAlchemy(app)

from backend import routes

#TODO: add system of user login,
# flash cards,
# option to choice vocabulary of translate or mean