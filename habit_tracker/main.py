import os
import requests
from dotenv import load_dotenv
load_dotenv()

PIXELA_TOKEN = os.environ["PIXELA_TOKEN"]
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "clssadik"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.status_code)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : "graph231242342351",
    "name" : "Activity Graph",
    "type" : "commit",
    "color" : "ichou"
}

response = requests.post(graph_endpoint,json=graph_config)
print(response.text)

