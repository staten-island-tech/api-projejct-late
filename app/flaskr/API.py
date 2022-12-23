import requests
import json

data = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m").json()


data2=data['hourly']
print(data2)
for i in data2['time']:
    print(i)