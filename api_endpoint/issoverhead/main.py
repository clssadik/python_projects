import requests
from datetime import datetime

MY_LAT = 41.0707456
MY_LONG = 29.0509414

response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
response_iss.raise_for_status()
data = response_iss.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Europe/Istanbul"

}

response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response_sun.raise_for_status()
data = response_sun.json()
print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise," ",sunset)

time_now = datetime.now()

print(time_now)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

# if iss_latitude-5 <= MY_LAT <= iss_latitude+5 and iss_longitude-5 <= MY_LONG <= iss_longitude+5:


