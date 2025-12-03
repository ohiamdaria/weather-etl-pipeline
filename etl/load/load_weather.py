import os
from sqlalchemy import create_engine
import pandas as pd

def load_weather(data):
  print(data.to_sql("weather_data", engine, if_exists="append", index=False))
  with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print("Connection is OK")
  return 0


if __name__ == '__main__':
  data = pd.read_csv("/Users/dashakoroleva/weather-etl-pipeline/etl/transform/transform_weathercd ", sep=",")
  connection_string = "postgresql://weather_user:weather_pass@localhost:5432/weather_db"
  engine = create_engine(connection_string)

  load_weather(data)
