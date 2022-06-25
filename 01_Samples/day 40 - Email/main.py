import requests

SHEETY_EMAIL_EP = 'https://api.sheety.co/cb27c088bac4a933fc8a34f54bcc2d2d/flightDeals/users'

print("Welcome to Ranga's Flight Club.\n")
print("We find the best flight deals and email you.")
fname = input("What is your first name?\n")
lname = input("What is your last name?\n")
email_1 = input("What is your email?\n")
email_2 = input("Type your email ?\n")
print(fname, lname)
if email_2 == email_1:
    print("You're in the club...")
    users_data = {
        "user": {
            "firstName": fname,
            "lastName": lname,
            "email": email_1,
        }
    }
    response = requests.post(url=SHEETY_EMAIL_EP, json=users_data)
    print(response.text)
else:
    print("Emails do not match....")
