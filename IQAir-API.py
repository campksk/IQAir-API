import requests

key = "483a1f6e-0d6b-4e06-9e5d-56848b7ee555"
lat = "13.115039"
lon = "99.939195"
url = "https://api.airvisual.com/v2/nearest_city?lat=" + lat + "&lon=" + lon + "&key=" + key

print(url)
response = requests.get(url)
print(response.json())