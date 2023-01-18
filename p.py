import json
import requests

data = requests.get('https://api.spoonacular.com/recipes/654959/information?includeNutrition=false&apiKey=8f76aac47cef4f23874744431bd6424a').json()

print(data)
