import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()

API_KEY = os.getenv("API_KEY")
LAT = 36.771297
LONG = 34.569662
URL = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(URL, params=params)
data = response.json()

current_temp = data["list"][0]["main"]["temp"]

print(response.status_code)

will_rain = False

for i in range(0, 5):
    if data["list"][i]["weather"][0]["id"] > 700:
        will_rain = True
    # else:
    #     print("Don't you dare :) ")

if will_rain:
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="yağmur yağıyor mevcut sıcaklık : ",
        to='whatsapp:+905073519085'
    )

    print(message.status)