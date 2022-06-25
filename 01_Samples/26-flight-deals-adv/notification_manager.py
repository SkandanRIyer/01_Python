from pprint import pprint

from twilio.rest import Client
import smtplib
import requests

TWILIO_SID = 'AC1e39fb4011e504b2e4eac0bb6017d889'
TWILIO_AUTH_TOKEN = 'c830bd4cf07c851950dbbe46ef04a839'
TWILIO_VIRTUAL_NUMBER = '+19124202896'
TWILIO_VERIFIED_NUMBER = '+919500080348'
USERNAME = "sriyer2009@gmail.com"
PASSWORD = 'Sadhguru@isha99'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(USERNAME, PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=USERNAME,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )

