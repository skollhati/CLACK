from app.orm.orm_user import *

class Accounts:

    def __init__(self):
        pass

    def sign_in(self, team, email, password):
        """
        :param team: 소속 팀명
        :param email: 유저 이메일
        :param password: 계정 비밀번호
        :return: bool(존재 - True / 없음 - False)
        """
        user = User.query.filter(and_(User.password == password, User.email == email, User.team == team)).first()
        if user is not None:
            return True
        else:
            return False

    def team_check(self, team, email):
        """
        index페이지 Team 체크 통해서 체크 후 가입 페이지로 REDIRECT

        :param team: 소속팀
        :param email: 유저 이메일
        :return: bool(존재 - True / 없음 - False)
        """
        if User.query.filter(and_(User.team == team, User.email == email)).first() is not None:
            return True
        else:
            return False

    def sign_up(self, team, email, password, nickname):
        #TODO: NickName Password 추가 입력 후 가입
        db.session.add(User(team, email, nickname, password))

    def sign_out(self, team, email, token):
        #TODO: 로그아웃. Redis 세션에서 삭제
        pass
