import requests

SHEETY_PUT_EP = 'MY_SHEET_PUT'
SHEETY_GET_EP = "MY_SHEET_GET"


class DataManager:

    def __init__(self):
        pass

    def update_row(self, city: dict):
        rowid = city['id']
        ep = f"{SHEETY_PUT_EP}{rowid}"
        print(ep)
        price = {
            "price": city
        }
        response = requests.put(url=ep, json=price)
        print(response.text)

    def get_destinations(self):
        response = requests.get(url=SHEETY_GET_EP)
        response.raise_for_status()
        return response.json()['prices']
