import time

from googlemaps import Client as GoogleMaps
import pandas as pd

gmaps = GoogleMaps('AIzaSyA5wBAk3ygtDdDl-U-Vop0cRJzNFcng4Qo')

addresses = pd.read_csv("address.csv")
addresses['long'] = ""
addresses['lat'] = ""
for (index, row) in addresses.iterrows():
    try:
        time.sleep(1) #to add delay in case of large DFs
        geocode_result = gmaps.geocode(row.FullAddress)
        row.lat = geocode_result[0]['geometry']['location'] ['lat']
        print(row.lat)
        row.long = geocode_result[0]['geometry']['location']['lng']
        print(row.long)
    except IndexError:
        print("Address was wrong...")
    except Exception as e:
        print("Unexpected error occurred.", e )

print(addresses.head())
addresses.to_csv("Final_List.csv")