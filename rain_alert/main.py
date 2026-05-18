import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
LAT = 36.771297
LONG = 34.569662
URL = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY
}

response = requests.get(URL, params=params)
data = response.json()

print(response.status_code)

will_rain = False

for i in range(0, 5):
    if data["list"][i]["weather"][0]["id"] > 700:
        will_rain = True
    else:
        print("Don't you dare :) ")

if will_rain:
    print("Bring an umbrella")