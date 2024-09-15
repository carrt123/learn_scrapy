import requests
import base64
import json
data = {
    "username": "admin",
    "password": "admin"
}

url = "https://login1.scrape.center/"

response = requests.get(url, data={'token': base64.b64encode(json.dumps(data).encode("utf-8"))})
print(response.text)
print(response.status_code)
