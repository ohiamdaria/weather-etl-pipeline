import pandas as pd
df = pd.read_json("raw_weather.json")
print(df.head())
print(df.columns)
print(df.info())
print(df)
df["temp"] = df["main"].apply(lambda x: x["temp"])
for column in df.columns:
	print(column)
	print(df[column].isna().sum())

print(df.head(1))
