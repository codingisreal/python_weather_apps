from flask import Flask
import requests

app = Flask(__name__)

 #Defining the weather data by giving openweather url and API key
def weather_data(query):
    res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=9c90d26c16c77d8b3cec65059d078841&units=metric');
    return res.json();

@app.route('/weather/<cityname>')
def get_weatherinfo(cityname):
  #returns the weatherinfo
     try:
         print('cityname: '+ cityname);
         print('cityname2: '+ cityname);
         query='q='+cityname;
         w_data=weather_data(query);
         return w_data;

     except:
         print('City name not found...');
