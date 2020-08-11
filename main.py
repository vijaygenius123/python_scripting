import requests

url = 'http://jsonplaceholder.typicode.com/photos'

resp = requests.get(url)

print(resp.json())