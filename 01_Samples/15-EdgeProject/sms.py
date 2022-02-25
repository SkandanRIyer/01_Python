from twilio.rest import Client
from places import Places
import pandas

class Message:

    def __init__(self):
        self.account_sid = "MY_API"
        self.auth_token = "MY_API"
        self.place = Places()

    def trigger_sms(self, phone, hospitals):
        client = Client(self.account_sid, self.auth_token)
        for num in range(len(hospitals["name"])):
            h_name = hospitals["name"][num]
            h_number = hospitals["number"][num]
            message = client.messages \
                .create(
                body=f"Emergency care available at {h_name}. Contact {h_number}",
                from_='+19124202896',
                to=f"+91{phone}"
            )

    def send_alert(self, patient_name):
        final_list = pandas.read_csv("Final_List.csv")
        for (index, row) in final_list.iterrows():
            if row["name"] == patient_name:
                hospitals = self.place.find_hospitals(row["lat"], row["long"])
                self.trigger_sms(row["contactnumber"], hospitals)
