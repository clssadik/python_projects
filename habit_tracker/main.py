import os
import requests
from datetime import date
from dotenv import load_dotenv
load_dotenv()

PIXELA_TOKEN = os.environ["PIXELA_TOKEN"]
USERNAME = "clssadik2"
pixela_endpoint = "https://pixe.la/v1/users"
graph_id = "activity-graph"
GRAPH_URL = "https://pixe.la/v1/users/clssadik2/graphs/activity-graph.html"

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"

today = date.today().strftime("%Y%m%d")

pixel_config = {
    "date": today,
    "quantity": "20",
}

pixel_config_2 = {
    "quantity": "5",
}

update_endpoint = f"{pixel_endpoint}/20260530"

# response = requests.post(pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

response = requests.put(update_endpoint, json=pixel_config_2, headers=headers)
print(response.text)

delete_endpoint = f"{pixel_endpoint}/20260530"
response = requests.delete(delete_endpoint, headers=headers)
print(response.text)