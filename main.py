import requests

url = 'http://jsonplaceholder.typicode.com/photos'

#resp = requests.get(url)

#print(resp.json())

jsonPayload  = {"albumId": 1, "title": "Test", "url": "nothing.com", "thumbailUrl": "nothing.com"}

resp = requests.post(url, json= jsonPayload)

print(resp.json())