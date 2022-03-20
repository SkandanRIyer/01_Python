import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com'
TEQUILA_LOCATIONS_API_EP = 'https://tequila-api.kiwi.com/locations/query'
TEQUILA_API_KEY = 'MY_TEQ'

class FlightSearch:

    def __init__(self):
        pass

    def get_iataCode(self, city: str):
        header = {
            "apiKey": TEQUILA_API_KEY,
        }
        query_data = {
            "term": city,
            "location_types": "city",
        }
        response = requests.get(url=TEQUILA_LOCATIONS_API_EP, headers=header, params=query_data)
        return response.json()["locations"][0]["code"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data