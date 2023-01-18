import json
import requests

data = requests.get('https://api.spoonacular.com/recipes/random?number=1&apiKey=8f76aac47cef4f23874744431bd6424a').json()

i=(data['recipes'])
print (i)

