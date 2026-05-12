import requests
import json

response = requests.get("https://opentdb.com/api.php?amount=10")


question_data = response.json()

print(type(question_data))