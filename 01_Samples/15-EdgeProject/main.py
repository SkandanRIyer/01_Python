import pandas
from googleplaces import GooglePlaces, types
import requests
import json
# Step1 : Get the coordinates for the addresses
# This is done by running he address_converter.py everytime an address is added

API_KEY = 'AIzaSyA5wBAk3ygtDdDl-U-Vop0cRJzNFcng4Qo'
google_places = GooglePlaces(API_KEY)
#TODO: If abnormalities found, send SMS to the relative mentioned in the list, with the list of top 2 hospitals
#      If hospital already in the contact details, check whether open and inform this in SMS


def get_place_details(place_id, fields):
    endpoint_url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        'placeid': place_id,
        'fields': ",".join(fields),
        'key': API_KEY
    }
    res = requests.get(endpoint_url, params=params)
    place_details = json.loads(res.content)
    return place_details


def find_hospitals(lat, long):
    query_result = google_places.nearby_search(
        lat_lng ={'lat': lat, 'lng': long},
        radius=5000,
        types=[types.TYPE_HOSPITAL])

    # If any attributions related
    # with search results print them
    if query_result.has_attributions:
        print(query_result.html_attributions)

    # Iterate over the search results
    for place in query_result.places:
        fields = ['name', 'formatted_address', 'international_phone_number', 'website', 'rating', 'review']
        details = get_place_details(place.place_id, fields)
        key = "international_phone_number"
        if key in details["result"]:
            print(details["result"]["international_phone_number"])
            print(place.name)
        # print("Latitude", place.geo_location['lat'])
        # print("Longitude", place.geo_location['lng'])



def trigger_sms(phone):
    # TODO: Send SMS
    print("Sending SMS......")



def send_alert(name):
    final_list = pandas.read_csv("Final_List.csv")
    for (index, row) in final_list.iterrows():
        if row["name"] == name:
            find_hospitals(row["lat"], row["long"])
            trigger_sms(row["contactnumber"])


# Step 2: Get the fitbit data for the elders being monitored once in configured minutes
heart_rate = pandas.read_csv("id-1003_heartrate_15min_20171001_20171007.csv")
for (ind, r) in heart_rate.iterrows():
    if r["Value"] >= 90:
        name = r["name"]
        send_alert(name)




