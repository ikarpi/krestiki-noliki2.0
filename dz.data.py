import pandas as pd

df = pd.read_csv('players_data_light-2024_2025.csv')

print(df.head())
print(df.info())
print(df.describe())

