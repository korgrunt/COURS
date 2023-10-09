import requests
import json

url = "https://data.att.ovh/lmdw.json"

response = requests.get(url)

#print(response)
#print(response.headers)
#print(response.status_code)
data = response.json()

file_name = "lmdw.json"

with open(file_name, 'w', encoding="utf-8") as f:
    json.dump(data, f, indent=4)
