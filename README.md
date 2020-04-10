# Ingreedy Foodmap

Code for preparing a food map for Ingreedy.

Installation:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 1. Turn McCance XLSX spreasheet into minimal CSV and JSON

Open in Libre Office then save the "Proximates" sheet as a CSV file in _data/raw_.

Then run this to generate a CSV and JSON with just the food nutrient data we need:

```bash
python build_foodsearch.py
```

## 2. Normalize NYT ingredient food names

(Note: it would be better to do this in Javascript, so we are sure the normalization is identical.)

```bash
python normalize_nyt_food_names.py
```

## 3. Manually map food names to database food entries

This is done by going through each food name and assigning it to a food in the database.

See https://docs.google.com/spreadsheets/d/1wEZqp9394Bobxl4W8__99i2OcAxBt2pARnoG-3j0u8E/edit#gid=582435857

## 4. Build the foodmap file

Download the "foodmap" sheet as a CSV file and save in _data/processed_

```bash
mv "/Users/tom/Downloads/foodmap - foodmap.csv" data/processed/
python build_foodmap.py
```
