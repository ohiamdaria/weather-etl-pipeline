import os
import pandas
import datetime

def transform_weather(data):
	data = data.dropna()
	
	
	
	return data

if __name__ == "__main__":
	data = pandas.read_json("../../data/raw_weather.json")
	data = transform_weather(data)
	data.to_csv("transform_weather")

