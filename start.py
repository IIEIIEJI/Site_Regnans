__author__ = 'timur'
from app import app
from gevent.wsgi import WSGIServer
from gevent import monkey; monkey.patch_all()
app.debug = True
http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()