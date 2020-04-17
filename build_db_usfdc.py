import pandas as pd

if __name__ == '__main__':
    foods = pd.read_csv("data/raw/FoodData_Central_sr_legacy_food_csv_ 2019-04-02/food.csv")

    nutrients = pd.read_csv("data/raw/FoodData_Central_sr_legacy_food_csv_ 2019-04-02/food_nutrient.csv")
    # Nutrient IDs are from data/raw/FoodData_Central_Supporting_Data_csv_ 2019-04-02/nutrient.csv, see below
    nutrients = nutrients[nutrients['nutrient_id'].isin(["1003", "1004", "1005", "1008", "1079"])]
    nutrients = nutrients[["fdc_id", "nutrient_id", "amount"]]
    nutrients = nutrients.pivot(index="fdc_id", columns="nutrient_id", values="amount")

    foods = pd.merge(foods, nutrients, how="inner", on="fdc_id", right_index=False, left_index=False)
    foods = foods.rename(columns={
        "fdc_id": "food_code",
        "description": "name",
        "food_category_id": "group",
        1003: "protein",
        1004: "fat", # Total lipid (fat)
        1005: "carbs", # Carbohydrate, by difference
        1008: "energy", # Energy KCAL
        1079: "fibre" # Fiber, total dietary
    })
    foods = foods[["food_code", "name", "group", "protein", "fat", "carbs", "energy", "fibre"]]

    foods.to_csv('data/processed/usfdc_minimal.csv', index=False)
    foods.to_json('data/processed/usfdc.json', orient='records')
