# -*- coding: utf-8 -*-
from flask_mail import Message
from app import mail
from threading import Thread
from config import ADMINS

def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper

def send_async_email(msg):
    mail.send(msg)

def send_email(subject, html_body):
    msg = Message(subject, sender = ADMINS[0], recipients = ADMINS)
    msg.html = html_body
    send_async_email(msg)