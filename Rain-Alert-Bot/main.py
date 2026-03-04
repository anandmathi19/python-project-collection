import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = "Your Api Key"
account_sid = "Your Account Sid"
auth_token = "Your Auth Token"

weather_params = {
    "lat": 13.040478,
    "lon": 80.160359,
    "appid": api_key,
    "cnt": 4,
}


response = requests.get(OWM_Endpoint, params= weather_params)
response.raise_for_status()
weather_data = response.json()

#weather_id = weather_data['list'][0]['weather'][0]['id']
will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']

    if int(condition_code) < 700:
        will_rain = True

receivers =["whatsapp: Your Phone Number",
            "whatsapp: Your Phone Number"]
if will_rain:
    client = Client(account_sid, auth_token)
    for number in receivers:
        message = client.messages.create(
            body="It's going to rain today. Bring an umbrella ☔",
            from_="whatsapp: Your Twilio NUmber",
            to=number

    )

        print(message.status)





