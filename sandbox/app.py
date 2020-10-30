from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/greet')
def say_hello():
  return 'Hello from Server'

@app.route('/weather/<cityname>')
def show_user(cityname):
  #returns the username
  return 'CityName: %s' % cityname
