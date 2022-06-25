from flask import Flask, request
import requests

LATLONG_URl = "http://api.positionstack.com/v1/forward"
MY_KEY = "MYKEY"
MY_APPID = "MYAPP"

app = Flask(__name__)


@app.route('/getTemperature/<city>')
def hello(city):
    parameters = {
        "access_key": MY_KEY,
        "query": city,
    }

    response = requests.get(url=LATLONG_URl, params=parameters)
    response.raise_for_status()
    lat = response.json()["data"][0]["latitude"]
    long = response.json()["data"][0]["longitude"]

    weather_parameters = {
        "lat": lat,
        "lon": long,
        "exclude": "current,minutely,daily",
        "appid": MY_APPID,
    }

    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=weather_parameters)
    response.raise_for_status()
    weather_data = response.json()

    response ={
        "Weather Summary": '',
        "Weather Today": '',
    }
    for hour_weather in weather_data["hourly"][:12]:
        if int(hour_weather["weather"][0]["id"]) > 800:
            response["Weather Summary"] = "Generally Cloudy"
        elif int(hour_weather["weather"][0]["id"]) == 800:
            response["Weather Summary"] = "Generally Clear"
        elif int(hour_weather["weather"][0]["id"]) > 700:
            response["Weather Summary"] = "Hazy"
        elif int(hour_weather["weather"][0]["id"]) > 600:
            response["Weather Summary"] = "Snow"
        else:
            response["Weather Summary "] = "Awesome"

    response["Weather Today"] = weather_data["hourly"][:12]
    return response


if __name__ == "__main__":
    app.run()
