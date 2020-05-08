import requests
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client["food-api"]
collection = db["recipes"]


mainUrl = "https://zagorapi.yemek.com"
url = "/search/recipe?query=*&Start=0&Rows=12"

def clean(cat):
	errors = {
		"Vi̇deo": "Video",
		"Yöresel tari̇fler": "Yöresel tarifler",
		"Hamur i̇şi̇": "Hamur işi",
		"Prati̇k yemek": "Pratik yemek",
		"Şerbetli̇ tatli": "Şerbetli tatlı",
		"Pi̇lav": "Pilav",
		"Prati̇k sütlü tatli": "Pratik sütlü tatlı",
		"Tatli kurabi̇ye": "Tatlı kurabiye",
		"Kurabi̇ye": "Kurabiye",
		"Pi̇zza": "Pizza",
		"Bakli̇yat": "Bakliyat",
		"Çi̇kolatali tatli": "Çikolatalı tatlı",
		"Zeyti̇nyağli": "Zeytintağlı"
	}

	try:
		last = errors[cat]
	except:
		last = cat
	
	return last

while url:
	req = requests.get(mainUrl + url).json()
	url = req["Pagination"]["NextMaxUrl"]
	
	try:
		posts = req["Data"]["Posts"]
	except:
		continue

	for i in posts:
		title = i["TitleCustomized"]
		ingredients = i["RecipeIngredient"]
		instructions = i["RecipeInstruction"]
		category = i["Label"].capitalize()

		category = clean(category)

		data = {
			"title": title,
			"ingredients": ingredients,
			"instructions": instructions,
			"category": category
		}
		collection.insert_one(data)
