##################### Extra Hard Starting Project ######################
import random
import pandas
import datetime as dt
import smtplib

MY_EMAIL = "sriyer2009@gmail.com"
MY_PASS = "pass"

month = dt.datetime.now().month
day = dt.datetime.now().day
birthdays_df = pandas.read_csv("birthdays.csv", index_col=0)
for (_, row) in birthdays_df.iterrows():
    print(f"{row.month} {row.name}")
    if month == row.month and day == row.day:
        letter = "letter" + "_" + str(random.randint(1, 3)) + ".txt"
        try:
            with open(f"./letter_templates/{letter}") as letter_data:
                text = letter_data.read()
        except FileNotFoundError:
            print(f"File ./letter_templates/{letter} not found!!")
        else:
            text = text.replace("[NAME]", row.name)
            connect = smtplib.SMTP("smtp.gmail.com")
            connect.starttls()
            connect.login(user=MY_EMAIL, password=MY_PASS)
            connect.sendmail(from_addr=MY_EMAIL, to_addrs=row.email, msg=f"Subject: Happy Birthday {row.name}\n\n"
                                                                         f"{text}")
            connect.close()
