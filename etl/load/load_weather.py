import os
from sqlalchemy import create_engine, text
import pandas as pd

def load_weather(data, engine):
  print(f"Load {len(data)} строк...")
  if 'Unnamed: 0' in data.columns:
        data = data.drop(columns=['Unnamed: 0'])
  data.to_sql("weather_data", engine, if_exists="append", index=False)
  with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    count = result.fetchone()[0]
    print(f"Table has {count} strings")
  return 0


if __name__ == '__main__':
  data = pd.read_csv("../transform/transform_weather.csv")
  connection_string = "postgresql+psycopg2://postgres@localhost:5432/weather_db"
  engine = create_engine(connection_string)

  load_weather(data, engine)
