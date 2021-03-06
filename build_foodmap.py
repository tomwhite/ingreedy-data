import pandas as pd

foodmap = pd.read_csv("data/processed/foodmap - foodmap.csv")
foodmap = foodmap[["normalized_name", "counts", "food", "food_afcd", "food_usfdc", "notes"]]

#foodmap.to_csv('data/processed/foodmap.csv', index=False)
foodmap.to_json('data/processed/foodmap.json', orient='records')

