import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 41.0707456
MY_LONG = 29.0509414

my_email = "cillsadik@gmail.com"
password = "emzusgkhexoikqao"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Europe/Istanbul"
}

while True:

    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data = response_iss.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    data_sun = response_sun.json()
    sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if iss_latitude-5 <= MY_LAT <= iss_latitude+5 and iss_longitude-5 <= MY_LONG <= iss_longitude+5:
        
        if sunset <= time_now.hour <= 24 or 0 <= time_now.hour <= sunrise:

            with open("example.txt") as file:
                icerik = file.read()
                
                with smtplib.SMTP("smtp.gmail.com",587) as connection:
                    connection.starttls()
                    connection.login(user=my_email,password=password)
                    connection.sendmail(
                        from_addr=my_email,
                        to_addrs="22220030090@mersin.edu.tr",
                        msg=f"Subject:Look Up!\n\n{icerik}".encode("utf-8")
                    )
    time.sleep(60)

