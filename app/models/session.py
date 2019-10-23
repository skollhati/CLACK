"""
    Session
    token:{
        email:
        nickname:
        team:
    }
"""
class Session:

    def __init__(self, team, nickname, email, token):
        self.email = email
        self.token = token
        self.nickname = nickname
        self.team = team

    def __repr__(self):
        return "Session<Team:{team} | Nick:{nickname} | email:{email} | token:{token}>".format(**self.__dict__)

