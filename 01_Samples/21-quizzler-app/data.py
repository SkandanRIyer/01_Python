import requests


def generate_data():
    # fill Question Data
    parameters = {
        "amount": 10,
        "type": "boolean",
    }
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    question_data = response.json()["results"]
    return question_data

