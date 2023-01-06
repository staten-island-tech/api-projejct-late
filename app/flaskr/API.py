import requests
import json

data = requests.get("https://api.spoonacular.com/recipes/complexSearch?yogurt=pasta&apiKey=8f76aac47cef4f23874744431bd6424a").json()


print(data)