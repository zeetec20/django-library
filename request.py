import requests

response = requests.get("https://libraryzeetec20.herokuapp.com/api")
print(response.json())
