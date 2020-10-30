from flask import Flask
import requests

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
  #return 'CityName: %s' % cityname
  res=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cityname+'&APPID=9c90d26c16c77d8b3cec65059d078841&units=metric');
  return res.json();
