import requests
from bs4 import BeautifulSoup

url = "https://zagorapi.yemek.com/search/recipe?query=*&Start=0&Rows=12"


req = requests.get(url).json()
title = req["Data"]["Posts"][0]["TitleCustomized"]
print(title)
