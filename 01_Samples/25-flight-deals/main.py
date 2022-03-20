# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager

CHENNAI_IATA_CODE = "LON"

flight_search = FlightSearch()
dm = DataManager()
notification_manager = NotificationManager()

sheet_data = dm.get_destinations()
for city in sheet_data:
    if city['iataCode'] == '':
        city['iataCode'] = flight_search.get_iataCode(city['city'])
        print(city['iataCode'])
        dm.update_row(city)
    sheet_data = dm.get_destinations()

today = datetime.now() + timedelta(2)
six_month_from_today = datetime.now() + timedelta(6 * 30)

for destination in sheet_data:
    flight = flight_search.check_flights(
        CHENNAI_IATA_CODE,
        destination["iataCode"],
        from_time=today,
        to_time=six_month_from_today
    )

    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
