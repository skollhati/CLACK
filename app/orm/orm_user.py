from . import *


class User(db.Model):

    __tablename__ = 'users'

    idx = db.db.Column(db.Integer, primary_key=True, )
    team = db.Column(db.String(45))
    email = db.Column(db.String(45))
    nickname = db.Column(db.String(10))
    password = db.Column(db.String(64))

    def __init__(self, team, email, nickname, password):
        self.team = team
        self.email = email
        self.nickname = nickname
        self.password = password

    def __repr__(self):
        return "<User({idx}, {team}, {email}, {nickname})>".format(**self.__dict__)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.db.Columns}
