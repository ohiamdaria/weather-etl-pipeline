import os
import pandas as pd
import datetime
import json

def transform_weather(data):
	data['weather_description'] = data['weather'].apply(
        lambda x: x[0]['description'] if isinstance(x, list) and len(x) > 0 else None
    )
	useful_columns = ['city', 'extracted_at', 'weather_description', 'main.temp', 'main.feels_like', 'main.pressure', 'wind.speed']

	data = data[useful_columns]
	data.columns = useful_columns = ['city', 'extracted_at', 'weather_description', 'main_temp', 'main_feels_like', 'main_pressure', 'wind_speed']
	data = data.drop_duplicates()
	print(f"Количество явных дубликатов: {data.duplicated().sum()} ")
	data = data.dropna()
	print(f"Количество Nan-значений: {data.isna().sum()} ")
	return data

if __name__ == "__main__":
	with open("../../data/raw_weather.json", "r") as f:
		raw_data = json.load(f)
	data = pd.json_normalize(raw_data)
	data = transform_weather(data)
	data.to_csv("transform_weather.csv")

