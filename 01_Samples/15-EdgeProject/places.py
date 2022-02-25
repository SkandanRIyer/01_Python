from googleplaces import GooglePlaces, types
import requests
import json


class Places:

    def __init__(self):
        self.api_key = 'MY_API'
        self.google_places = GooglePlaces(self.api_key)

    def get_place_details(self, place_id, fields):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = {
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': self.api_key
        }
        res = requests.get(endpoint_url, params=params)
        place_details = json.loads(res.content)
        return place_details

    def find_hospitals(self, lat, long):
        query_result = self.google_places.nearby_search(
            lat_lng={'lat': lat, 'lng': long},
            radius=5000,
            types=[types.TYPE_HOSPITAL])

        # If any attributions related
        # with search results print them
        if query_result.has_attributions:
            print(query_result.html_attributions)
        hospitals_nearby = {"name": [], "number": []}
        # Iterate over the search results
        for place in query_result.places:
            fields = ['name', 'formatted_address', 'international_phone_number', 'website', 'rating', 'review']
            details = self.get_place_details(place.place_id, fields)
            key = "international_phone_number"
            if key in details["result"]:
                hospitals_nearby["name"].append(place.name)
                hospitals_nearby["number"].append(details["result"]["international_phone_number"])
        return hospitals_nearby
