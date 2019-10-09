import requests

response = requests.get("http://127.0.0.1:8080/api/book/?format=json")
print(response.json())
