import requests
import json

r = requests.get("https://pokeapi.co/api/v2/pokemon/charmander").json()
print(r)