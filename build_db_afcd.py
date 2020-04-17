import pandas as pd

if __name__ == '__main__':
    foods = pd.read_csv("data/raw/Release 1 - Food nutrient database.csv", skiprows=[1])
    foods = foods.rename(columns={
        "Public Food Key": "food_code",
        "Food Name": "name",
        "Classification": "group",
        "Protein": "protein",
        "Total Fat": "fat",
        "Available carbohydrate, without sugar alcohols": "carbs",
        "Energy, with dietary fibre": "energy",
        "Total dietary fibre": "fibre"
    })
    foods = foods[["food_code", "name", "group", "protein", "fat", "carbs", "energy", "fibre"]]
    foods.to_csv('data/processed/afcd_minimal.csv', index=False)
    foods.to_json('data/processed/afcd.json', orient='records')


