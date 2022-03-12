import requests
from datetime import datetime
import smtplib
import time
from config import *


def send_email():
    connect = smtplib.SMTP("smtp.gmail.com")
    connect.starttls()
    connect.login(user=MY_EMAIL, password=MY_PASS)
    connect.sendmail(to_addrs=MY_EMAIL, from_addr=MY_EMAIL, msg="Subject: ISS is nearby...Look up....👍👍👍\n\n"
                                                                f"Enjoy watching the ISS...{datetime.now()}")
    connect.close()


def iss_is_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(f"{iss_longitude} {iss_latitude}")
    print(f"{MY_LONG} {MY_LAT}")
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and \
            (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True
    return False


def is_night_now():
    # Your position is within +5 or -5 degrees of the ISS position.
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    if is_night_now() and iss_is_near():
        send_email()
    time.sleep(60)
