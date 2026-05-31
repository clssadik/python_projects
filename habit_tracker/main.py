import os
import requests
from datetime import date
from dotenv import load_dotenv
load_dotenv()

PIXELA_TOKEN = os.environ["PIXELA_TOKEN"]
USERNAME = "clssadik2"
pixela_endpoint = "https://pixe.la/v1/users"
graph_id = "activity-graph"

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"

today = date.today().strftime("%Y%m%d")

pixel_config = {
    "date": today,
    "quantity": "20",
}


response = requests.post(pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
    
