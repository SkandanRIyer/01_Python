import requests
from twilio.rest import Client

account_sid = "MY_SID"
auth_token = "MY_TOKEN"

MY_KEY = "MY_KEY"
MY_CITY = "Chennai, India"
MY_LAT = 12.984800
MY_LONG = 80.258171



parameters = {
    "lat": -7.966620,
    "lon": 110.4381,
    "exclude": "current,minutely,daily",
    "appid": MY_KEY,
}

# response = requests.get(url="http://api.openweathermap.org/data/2.5/weather", params=parameters)
# response.raise_for_status()
# print(response.json())

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

it_will_rain = False

for hour_weather in weather_data["hourly"][:12]:
    if int(hour_weather["weather"][0]["id"]) < 700:
        it_will_rain = True

if it_will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's  Raining Today! Bring an Umbrella!!☔☔",
        from_='+19124202896',
        to='+919500080348'
    )

    print(message.status)