import requests
import json

r = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m").json()
print(r)