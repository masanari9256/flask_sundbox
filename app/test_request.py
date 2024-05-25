import json
import requests

url = "https://jsonplaceholder.typicode.com/posts/"

headers = {
    "Content-type": "application/json; charset=UTF-8"
}

data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

res = requests.post(url, headers=headers, data=json.dumps(data))
print(res.json())
