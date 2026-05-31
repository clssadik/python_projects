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
    "quantity": "1",
}

for _ in range(10):
    response = requests.post(pixel_endpoint, json=pixel_config, headers=headers)
    data = response.json()
    if data.get("isSuccess"):
        print("Success:", today)
        break
    elif data.get("isRejected"):
        print("Rejected, retrying...")
    else:
        print(data)
        break
