import requests
import json

key = "API-KEY"
lat = "13.115039"
lon = "99.939195"
url = "https://api.airvisual.com/v2/nearest_city?lat=" + lat + "&lon=" + lon + "&key=" + key

data = requests.get(url).json()

pollution = data['data']['current']['pollution']

ts = pollution['ts']
aqius = pollution['aqius']
mainus = pollution['mainus']
aqicn = pollution['aqicn']
maincn = pollution['maincn']

print(ts)
print(aqius)
print(mainus)
print(aqicn)
print(maincn)