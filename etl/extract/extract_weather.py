import requests
import json
from datetime import datetime
import os

def extract_weather(api_key, cities):

	data = []
	for city in cities:
		url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
		response = requests.get(url)
		if response.status_code == 200:
			weather = response.json()
			weather['city'] = city
			weather['extracted_at'] = datetime.now().isoformat()
			data.append(weather)
			with open("../data/raw_weather.json", "w") as f:
				json.dump(data, f, indent=2)
			print(f"Extracted data for {len(data)} cities")
	return 1 if len(data) > 0 else 0 

if __name__ == "__main__":
	API_KEY = "ade6c6ea1ce75ee42984e411e93bf8f1"
	cities = ["Moscow", "Saint Petersburg", "Novosibirsk", "Kazan"]
	result = extract_weather(API_KEY, cities)
	if result == 0:
		print("Something went wrong")



