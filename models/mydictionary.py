from app import db


class MyDictionary(db.Model):

    __tablename__ = 'dictioanry_en_pt'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String)
    translate = db.Column(db.String)

    def __repr__(self):
        return '{} = {}'.format(self.word, self.translate)