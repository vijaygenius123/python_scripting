import requests

url = 'http://jsonplaceholder.typicode.com/photos'

response = requests.get(url)

json_response = response.json()

photos_list = []

for obj in json_response:
    photos_list.append(obj["thumbnailUrl"])

total_pics = len(photos_list)
pics_without_duplicate = len(set(photos_list))

print("Total Pics: {}\nOriginal Pics : {}\nDuplicate: {}".format(total_pics, pics_without_duplicate, total_pics - pics_without_duplicate))
