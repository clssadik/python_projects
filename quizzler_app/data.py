import requests
import json

response = requests.get("https://opentdb.com/api.php?amount=10")
question_data = response.json()

with open("data.json","w") as file:
    json.dump(question_data,file,indent=4)