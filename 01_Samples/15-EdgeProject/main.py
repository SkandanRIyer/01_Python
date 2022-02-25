import pandas
import sms
import places

# Step1 : Get the coordinates for the addresses
# This is done by running he address_converter.py everytime an address is added
place = places.Places()
sms = sms.Message()
# Step 2: Get the fitbit data for the elders being monitored once in configured minutes
heart_rate = pandas.read_csv("id-1003_heartrate_15min_20171001_20171007.csv")
for (ind, r) in heart_rate.iterrows():
    if r["Value"] >= 90:
        name = r["name"]
        sms.send_alert(name)
