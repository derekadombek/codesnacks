from flask import Flask
import requests

app = Flask(__name__)

API_KEY = "05b16af40054e9afa559888d0f10a897"

@app.route('/')
def index():
    return 'App Works!'

@app.route('/<string:city>/<string:country>/')
def weather_by_city(city,country):

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=imperial&appid={API_KEY}'

    response = requests.get(url=url)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)