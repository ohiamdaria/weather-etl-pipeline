import os
import pandas as pd
from extract.extract_weather import extract_weather
from load.load_weather import load_weather

from sqlalchemy import create_engine, text

if __name__ == '__main__':
  API_KEY = "ade6c6ea1ce75ee42984e411e93bf8f1"
  cities = ["Moscow", "Saint Petersburg", "Novosibirsk", "Kazan"]
  result_extract = extract_weather(API_KEY, cities)
  if result_extract == 1:
    print("Extract completed OK")
  else:
    print("Something went wrong")

  data = pd.read_csv("transform/transform_weather.csv")
  connection_string = "postgresql+psycopg2://postgres@localhost:5432/weather_db"
  engine = create_engine(connection_string)
  result_load = load_weather(data, engine)

  if result_load == 1:
    print("Load completed OK")
  else:
    print("Something went wrong")