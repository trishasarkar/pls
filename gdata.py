import requests

url = "https://api.npoint.io/c4b4edd3640ed8357987"

r = requests.get(url)
data = r.json()

print(data)
