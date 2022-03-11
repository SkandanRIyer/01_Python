# import smtplib
#
# my_email = "sriyer2009@gmail.com"
# password = "Sadhguru@isha99"
#
# connect = smtplib.SMTP("smtp.gmail.com")
# connect.starttls()
# connect.login(user=my_email, password=password)
# connect.sendmail(from_addr=my_email, to_addrs="sriyer2009@gmail.com", msg="Subject: Alert!!!Alert!!!\n\n"
#                                                                           "Hello Skandan! Do not waster time in "
#                                                                           "youtube!")
# connect.close()

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1979, month=6, day=2, hour=22, minute=30)
# print(date_of_birth)

import smtplib
import random
import datetime as dt

my_email = "sriyer2009@gmail.com"
password = "Sadhguru@isha99"

day_of_week = dt.datetime.now().weekday()
if day_of_week == 0:
    try:
        with open("quotes.txt") as quote:
            quotes = quote.readlines()
    except FileNotFoundError:
        print("Quotes files not found")
    else:
        send_quote = random.choice(quotes)
        connect = smtplib.SMTP("smtp.gmail.com")
        connect.starttls()
        connect.login(user=my_email, password=password)
        connect.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject: Monday Quotes \n\n"
                                                                        f"{send_quote}")
        connect.close()


