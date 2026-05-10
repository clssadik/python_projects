# import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude,latitude)

# print(iss_position)

import requests
from datetime import *

MY_LAT = 41.0707456
MY_LONG = 29.0509414

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

now = datetime.now()

print(now.hour)