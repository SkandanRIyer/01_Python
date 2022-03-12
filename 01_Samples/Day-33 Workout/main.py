import requests
import datetime as dt

# result = requests.get(url="http://api.open-notify.org/iss-now.json")
# result.raise_for_status()
# # print(result.json()["iss_position"])
#
# data = dict()
# data = result.json()
# print(data["iss_position"]["longitude"])
# print(data["iss_position"]["latitude"])

# result = requests.get(url="https://api.kanye.rest")
# result.raise_for_status()
# print(result.json())
MY_LAT = 12.984800
MY_LONG = 80.258171

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]
print(f"Sunrise : {sunrise} \nSunset: {sunset}")
time_now = dt.datetime.now()
hour = time_now.hour
print(hour)