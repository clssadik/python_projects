import os
import requests

PIXELA_TOKEN = os.environ["PIXELA_TOKEN"]
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": "clssadik",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(pixela_endpoint, json=user_params)
print(response.status_code)
