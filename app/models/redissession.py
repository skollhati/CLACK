from . import Redis_Module
from uuid import uuid4
import datetime
from flask.sessions import SessionInterface, SessionMixin
from werkzeug.datastructures import CallbackDict
import json


class Session(CallbackDict, SessionMixin):
    def __init__(self, initial=None, session_id=None):
        CallbackDict.__init__(self, initial)
        self.session_id = session_id


class RedisSessionInterface(SessionInterface):

    def __init__(self):
        self.redis = Redis_Module.RedisInterface.instance()
        self.redis.RegistRedisConnection('session', 1, '123456')
        self.session_redis = self.redis.GetRedisConnection('session')

    def open_session(self, app, request):
        session_id = request.cookies.get(app.session_cookie_name)
        if session_id:
            stored_session = self.session_redis.GetData(session_id)
            if stored_session:
                return Session(stored_session, session_id)

        session_id = str(uuid4())
        return Session(session_id=session_id)

    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        if session is None:
            self.session_redis.RemoveData(session.session_id)
            response.delete_cookie(app.session_cookie_name, domain=domain)
            return

        expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        session['expiration'] = str(expiration)
        self.session_redis.SetData(session.session_id, json.dumps(dict(session),ensure_ascii=False))
        response.set_cookie(app.session_cookie_name, session.session_id,
                            expires=expiration,
                            httponly=True, domain=domain
                            )
