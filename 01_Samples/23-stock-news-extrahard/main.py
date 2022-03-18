import datetime
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_PRICE_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"

account_sid = "MY_SID"
auth_token = "MY_TOKEN"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
yesterday = str(datetime.datetime.today() - datetime.timedelta(days=3)).split(" ")[0]
day_before = str(datetime.datetime.today() - datetime.timedelta(days=4)).split(" ")[0]

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "MY_KEY",
}

response = requests.get(url=STOCK_PRICE_URL, params=stock_parameters)
response.raise_for_status()
result = response.json()
change = round(
    (float(result["Time Series (Daily)"][yesterday]["4. close"]) - float(result["Time Series (Daily)"][day_before][ \
                                                                             '4. close'])) * 100 / float( \
        result["Time Series (Daily)"][day_before]["4. close"]), 2)
print(change)
if change >= 5.00 or change <= -5.00:
    news_parameters = {
        "q": COMPANY_NAME,
        "from": day_before,
        "to": yesterday,
        "apiKey": "7d72792a37024c41bba953939cf422f0",
    }
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

response = requests.get(url=NEWS_URL, params=news_parameters)
response.raise_for_status()
result = response.json()
news_data = result["articles"][0:3]
client = Client(account_sid, auth_token)
if change > 0:
    ctext = f"🔺{round(abs(change))}"
else:
    ctext = f"🔻{round(abs(change))}"
for news in news_data:
    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    print("Sending SMS....")
    headline = news["title"]
    brief = news["description"]
    print(f"{STOCK}: {ctext}\nHeadline:{headline}\nBrief:{brief}")
    message = client.messages \
        .create(
        body=f"{STOCK}: {ctext}\nHeadline:{headline}\nBrief:{brief}",
        from_="+19124202896",
        to="+919500080348"
    )
    print(message.status)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
