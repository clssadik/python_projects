import os
from dotenv import load_dotenv
load_dotenv()
import requests

URL = os.environ["BASE_URL"]
ID = os.environ["ID"]
KEY = os.environ["KEY"]
SHEETS = os.environ["SHEETS"]

json_params = {
    "query": "swam for 1 hour"
}

headers_params = {
    "Content-Type": "application/json",
    "x-app-id": ID,
    "x-app-key": KEY
}

response = requests.post(URL, headers=headers_params ,json=json_params)
print(response.status_code)
print(response.text) 