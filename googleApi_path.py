
import requests

endpoint = "https://maps.googleapis.com/maps/api/directions/json"

# For SiteID 387 -> Latitude (29.7604)	Longitude(-95.3698)
# For SiteID 405 -> Latitude (43.0389)	Longitude(-87.9065)
# key = AIzaSyDaBAWA3TJoUqovyChaDWo5FQbL-4Fi6x8

params = {
    "origin": "29.7604,-95.3698",
    "destination": "43.0389,-87.9065",
    "units": "imperial",
    "key": "AIzaSyDaBAWA3TJoUqovyChaDWo5FQbL-4Fi6x8"
}

response = requests.get(endpoint, params=params)
data = response.json()

if data["status"] == "OK":
    distance = data["routes"][0]["legs"][0]["distance"]["text"]
    time = data["routes"][0]["legs"][0]["duration"]["text"]
    print(time)

    print(distance)

else:
    print("Error:", data["status"])
