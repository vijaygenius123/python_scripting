import requests

url = "https://api.github.com/users/vijaygenius123"

response = requests.get(url)

print(response.text)