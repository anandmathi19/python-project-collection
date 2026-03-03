import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "Your API key"
NEWS_API_KEY = "Your Api key"

TWILIO_SID = "Your Token"
TWILIO_AUTH = "Your Auth"

STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()

daily_data = data["Time Series (Daily)"]
data_list = [value for (key, value) in daily_data.items()]
yesterday_data = data_list[0]
day_before_yesterday_data = data_list[1]

yesterday_closing_price = float(yesterday_data["4. close"])
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

diff = abs(yesterday_closing_price - day_before_yesterday_closing_price)

up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percentage = (diff/ day_before_yesterday_closing_price) * 100

news_params = {
    "qInTitle": COMPANY_NAME,
    "apikey": NEWS_API_KEY,
}

news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
articles= news_response.json()["articles"]
three_articles = articles[:3]

formatted_articles = [
    f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
                      for article in three_articles
]

if abs(diff_percentage) > 0:
    client = Client(TWILIO_SID, TWILIO_AUTH)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="whatsapp:+14155238886",
            to="whatsapp:+919962811465",
        )
        print(message.status)

else:
    print("No Major Change")

