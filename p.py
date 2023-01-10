import json
import requests

data = requests.get('https://api.spoonacular.com/recipes/complexSearch?query=pasta&number=100&apiKey=8f76aac47cef4f23874744431bd6424a').json()

print(data)
