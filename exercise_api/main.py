import os
from dotenv import load_dotenv
load_dotenv()
import requests
from datetime import datetime

URL = os.environ["BASE_URL"]
ID = os.environ["ID"]
KEY = os.environ["KEY"]
SHEETS = os.environ["SHEETS"]
AUTH = os.environ["AUTH"]

json_params = {
    "query": "swam for 1 hour"
}

headers_params = {
    "Content-Type": "application/json",
    "x-app-id": ID,
    "x-app-key": KEY
}

response_api = requests.post(URL, headers=headers_params ,json=json_params)
data_api = response_api.json()

duration = str(data_api["exercises"][0]["duration_min"])
calories = data_api["exercises"][0]["nf_calories"]
exercise = str(data_api["exercises"][0]["name"]).capitalize()
date = str(datetime.now().date())
time = str(datetime.now().time().strftime("%H:%M:%S"))

body = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

sheets_headers = {
    "Authorization" : AUTH,
}

response_sheets = requests.post(SHEETS, json=body, headers=sheets_headers)
print(response_sheets.status_code)