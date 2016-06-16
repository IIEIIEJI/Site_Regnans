#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'timur'
from uuid import uuid4
from datetime import datetime, timedelta
import hashlib,binascii

from flask.sessions import SessionMixin, SecureCookieSessionInterface
from werkzeug.datastructures import CallbackDict
from pymongo import MongoClient
class connect:

    def __init__(self,host='localhost', port=27017,
                 db='offenses', collection1='sessions',collection2='users',collection3='roles'):
        self.client = MongoClient(host, port)
        self.store1 = self.client[db][collection1]
        self.store2 = self.client[db][collection2]
        self.store3 = self.client[db][collection3]
    def __del__(self):
        self.client.close()
class MongoSession(CallbackDict, SessionMixin):

    def __init__(self, initial=None, sid=None):
        CallbackDict.__init__(self, initial)
        self.sid = sid
        self.modified = False
class MongoSessionInterface(connect,SecureCookieSessionInterface):
    #def __init__(self):
    #    connect.__init__(self)
    #def __del__(self):
    #    connect.__del__(self)
    def open_session(self, app, request):
        sid = request.cookies.get(app.session_cookie_name)
        if sid:
            stored_session = self.store1.find_one({'sid': sid})
            if stored_session:
                if stored_session.get('expiration') > datetime.utcnow():
                    return MongoSession(initial=stored_session['data'],
                                        sid=stored_session['sid'])
        sid = str(uuid4())
        return MongoSession(sid=sid)

    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        if 'username' not in session or not session:
            response.delete_cookie(app.session_cookie_name, domain=domain)
            #add delete session sid
            return
        if self.get_expiration_time(app, session):
            expiration = self.get_expiration_time(app, session)
        else:
            expiration = datetime.utcnow() + timedelta(hours=1)

        self.store1.update({'sid': session.sid},
                          {'sid': session.sid,
                           'data': session,
                           'expiration': expiration,
                           'username':session['username'],
                           'right':session['right']}, True)
        response.set_cookie(app.session_cookie_name, session.sid,
                            expires=expiration,
                            httponly=True, domain=domain)
class credential(connect):
    def credential(self,username,password):
        if self.store2.find_one({'username':username, 'password':binascii.hexlify(hashlib.pbkdf2_hmac('sha256',password,'lajdsofije09283lkjdf83j2lkjfm984ihkp09jalkdjf88u2093j ',100))}):
            return True
        else:
            return False
    def setrightskey(self,username,starttime):
        role=self.store2.find_one({'username':username}).get('role').encode()
        rightkey=self.store3.find_one({'role':role}).get('key').encode()
        return binascii.hexlify(hashlib.pbkdf2_hmac('sha256',str(starttime),rightkey,100))
    def getadminskey(self,starttime):
        rightkey=self.store3.find_one({'role':'admins'}).get('key').encode()
        return binascii.hexlify(hashlib.pbkdf2_hmac('sha256',str(starttime),rightkey,100))
