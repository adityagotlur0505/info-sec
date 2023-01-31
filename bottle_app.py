# A very simple Bottle Hello World app for you to get started with...
import os
from bottle import default_app, route, run

@route('/public')
def hello_public():
    return 'This is a  public message'
@route('/secret')
def hello_public():
    return 'This is a  secret message'

@route('/redirect')
def hello_public():
    return 'This is a  redirect message'
    
@route('/')
def hello_world():
    return 'Hello from Bottle!'

if 'PYTHONANYWHERE_DOMAIN' in os.environ:
    application = default_app()
else:
    run(host='localhost', port=8080)
