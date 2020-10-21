import os
import requests
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")


url = "https://api.github.com/user"

response = requests.get(url, headers={'Authorization': 'Bearer ' + TOKEN})

print(response.text)