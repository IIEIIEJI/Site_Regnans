__author__ = 'timur'
from flask import Flask, render_template,request,session, redirect, url_for, flash, render_template_string
from gevent.monkey import patch_all
patch_all()
from psycogreen.gevent import patch_psycopg
patch_psycopg()
using_gevent = True
app = Flask(__name__)
app.config.from_object('config')


@app.route("/")
def index():
   return render_template('index.html')

@app.route("/service")
def service():
   return render_template('service.html')

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

@app.route("/bspb-portfolio-single")
def bspb_portfolio_single():
   return render_template('bspb-portfolio-single.html')

@app.route("/inpas-portfolio-single")
def inpas_portfolio_single():
   return render_template('inpas-portfolio-single.html')

@app.route("/cbddmo-portfolio-single")
def cbddmo_portfolio_single():
   return render_template('cbddmo-portfolio-single.html')