from app import db

class Grocery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True)
    stock = db.Column(db.Integer)
    best_before = db.Column(db.Date, index=True)

    def __repr__(self):
        return '<Grocery {}>'.format(self.name)