#! /usr/bin/env python
# -*- coding: utf-8 -*-
from app import app
import time
from flask import render_template,request,session,redirect,flash,url_for
from emails import send_email
@app.route("/")
def index():
   return render_template('index.html')

@app.route("/service")
def service():
   return render_template('service/service.html')

@app.route("/service/infosecurity")
def infosecurity():
   return render_template('service/service_infosecurity.html')

@app.route("/service/itsystems")
def itsystems():
   return render_template('service/service_itsystems.html')

@app.route("/service/itsupport")
def itsupport():
   return render_template('service/service_itsupport.html')

@app.route("/service/consult")
def consult():
   return render_template('service/service_consult.html')

@app.route("/service/opensource")
def opensource():
   return render_template('service/service_opensource.html')

@app.route("/service/sales")
def sales():
   return render_template('service/service_sales.html')

@app.route("/contact")
def contact():
   return render_template('contact.html')

@app.route("/about")
def about():
   return render_template('about.html')

@app.route("/clients")
def clients():
   return render_template('clients.html')

@app.route("/partners")
def partners():
   return render_template('partners.html')

@app.route("/projects")
def projects():
   return render_template('projects.html')

@app.route("/test")
def test():
   return render_template('test.html')

@app.route("/jobs")
def jobs():
   return render_template('jobs.html')

@app.route('/vendors')
def vendors():
   if 'username' in session:
      return render_template('vendors.html')
   return redirect(url_for("login"))

@app.route('/licenses')
def licenses():
   return render_template('licenses.html')

@app.route('/send_mail', methods=['POST'])
def send():
   msg='Name:'+request.form['name']+' Email: '+request.form['email']+' Message:'+request.form['message']
   try:
      send_email(request.form['subject'],msg)
      return "OK"
   except:
      return "Ваш email не отправлен. Пожалуйста попробуйте позвонить нам!"

@app.route("/login",methods=['GET','POST'])
def login():
    error = None
    if 'username' in session:
       return redirect (url_for("index"))
    else:
        if request.method == 'POST':
            try:
                if rights.credential(request.form['httpd_username'],request.form['httpd_password']):
                    session.permanent=True
                    session['username']=request.form['httpd_username']
                    session['starttime']=time.time()
                    session['right']=rights.setrightskey(session['username'],session['starttime'])
                    return redirect(url_for("index"))
                else:
                    flash("Not authenticated")
            except: print "Can`t connect to DB"
    return render_template("login.html")

@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'), 404
