from backend import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String, )


class UserVocabulary(db.Model):
    __tablename__ = 'uservocabualary'
