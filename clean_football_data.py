import pandas as pd

df = pd.read_csv("footballData.csv")

print(df.head())

df = df.drop_duplicates()

df = df.dropna()

