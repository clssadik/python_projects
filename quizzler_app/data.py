import requests
import json

parameters = {
    "amount" : 10,
    "type" : "boolean"
}

response = requests.get("https://opentdb.com/api.php",params=parameters)
data = response.json()
question_data = data["results"]

# with open("data.json","w") as file:
#     json.dump(question_data,file,indent=4)

