# import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude,latitude)

# print(iss_position)

import requests

MY_LAT = 41.0707456
MY_LONG = 29.0509414

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)

data = response.json()
print(data)
