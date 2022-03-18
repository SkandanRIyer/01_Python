import datetime
import os

import requests

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
AUTHORIZATION = os.environ.get("AUTHORIZATION")
SHEETY_EP = os.environ.get("SHEETY_EP")

GENDER = "male"
WEIGHT_KG = 95
HEIGHT_CM = 180
AGE = 43

EXERCISE_EP = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
exercise_data = {
    "query": input("Enter your activity today: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
response = requests.post(url=EXERCISE_EP, json=exercise_data, headers=headers)
response.raise_for_status()
result = response.json()

for exercise in result["exercises"]:
    name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    date = datetime.datetime.now().strftime("%d/%m/%Y")
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{date} {time}")
    sheety_header = {
        "Authorization": AUTHORIZATION
    }
    sheety_data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": name,
            "duration": duration,
            "calories": calories,
        }
    }
    response = requests.post(url=SHEETY_EP, json=sheety_data, headers=sheety_header)
    response.raise_for_status()
    print(response.json())
