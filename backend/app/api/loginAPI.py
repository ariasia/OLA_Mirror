from flask import session
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from app.core import cas
from app.model import *


class LoginAPI(Resource):
    """
        Login Api Resource
    """

    def get(self):
        userInfo = self.getUserInfoFromCAS()

        if userInfo is not None:
            user = getUser(login=userInfo['login'])
            if user is not None and isUserAllowed(user["id"]):
                session['user'] = user
                return {'AUTH_RESULT': 'OK'}, 200
            else:
                return {'AUTH_RESULT': 'NOT_ALLOWED'}, 403
        else:
            return {'AUTH_RESULT': 'AUTHENTICATION_FAILED'}, 401

    def delete(self):
        session['user'] = None
        return {'AUTH_RESULT': 'OK'}, 200

    def getUserInfoFromCAS(self):
        if cas.username is not None:
            return {"login": cas.username}
        else:
            return None
