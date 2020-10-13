# models.py inside project directory
from project import db


class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    owner = db.relationship("Owner", backref="puppy", uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner == None:
            return "Puppy name: {}, and has not owner yet".format(self.name)
        return "Puppy name {}, and has owner: {}".format(self.name, self.owner.name)


class Owner(db.Model):

    __tablename__ = 'owner'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    id_pup = db.Column(db.Integer, db.ForeignKey("puppies.id"))

    def __init__(self, name, id_pup):
        self.name = name
        self.id_pup = id_pup
