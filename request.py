import requests

response = requests.get("https://libraryzeetec20.herokuapp.com/api/book/?format=json")
print(response.json())
