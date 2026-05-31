import os
import requests
from dotenv import load_dotenv
load_dotenv()

PIXELA_TOKEN = os.environ["PIXELA_TOKEN"]
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "clssadik2"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "activity-graph",
    "name": "Activity Graph",
    "unit": "commit",
    "type": "int",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN" : PIXELA_TOKEN
}

response = requests.post(graph_endpoint,json=graph_config, headers = headers)
print(response.text)

