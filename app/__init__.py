#! /usr/bin/env python
__author__ = 'timur'
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_mail import Mail
import app.initdb as db




using_gevent = True
app = Flask(__name__)
app.config.from_object('config')
mail=Mail(app)
rights = db.credential()

from app import views




