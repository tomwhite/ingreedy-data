import pandas as pd

foodmap = pd.read_csv("data/processed/foodmap - measures.csv")
foodmap = foodmap[["food", "unit", "weight"]]

foodmap.to_json('data/processed/measures.json', orient='records')

