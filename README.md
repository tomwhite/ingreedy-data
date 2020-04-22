# Ingreedy Data

Code for preparing data for [Ingreedy](https://github.com/tomwhite/ingreedy-js).

Installation:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 1. Turn food databases into CSV and JSON files

### McCance and Widdowson's 'composition of foods integrated dataset' (CoFID)

Download from https://www.gov.uk/government/publications/composition-of-foods-integrated-dataset-cofid.

Open in Libre Office then save the "Proximates" sheet as a CSV file in _data/raw_.

Then run this to generate a CSV and JSON with just the food nutrient data we need:

```bash
python build_db_mccance.py
echo -n "const mccance = " | cat - data/processed/mccance.json > data/processed/mccance_def.js
printf "\nmodule.exports = mccance\n" >> data/processed/mccance_def.js
```

### Australian Food Composition Database 

Download from https://www.foodstandards.gov.au/science/monitoringnutrients/afcd/Pages/default.aspx

Open in Libre Office then save the "All solids & liquids per 100g" sheet as a CSV file in _data/raw_.

Then run this to generate a CSV and JSON with just the food nutrient data we need:

```bash
python build_db_afcd.py
echo -n "const afcd = " | cat - data/processed/afcd.json > data/processed/afcd_def.js
printf "\nmodule.exports = afcd\n" >> data/processed/afcd_def.js
```

### US FoodData Central 

Download CSVs for SR Legacy from https://fdc.nal.usda.gov/download-datasets.html and save in _data/raw_.

Then run this to generate a CSV and JSON with just the food nutrient data we need:

```bash
python build_db_usfdc.py
echo -n "const usfdc = " | cat - data/processed/usfdc.json > data/processed/usfdc_def.js
printf "\nmodule.exports = usfdc\n" >> data/processed/usfdc_def.js
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
mv ~/Downloads/"foodmap - foodmap.csv" data/processed/
python build_foodmap.py
echo -n "const foods = " | cat - data/processed/foodmap.json > data/processed/foodmap_def.js
printf "\nmodule.exports = foods\n" >> data/processed/foodmap_def.js
```

## 5. Build the measures file

Download the "measures" sheet as a CSV file and save in _data/processed_

```bash
mv ~/Downloads/"foodmap - measures.csv" data/processed/
python build_measures.py
echo -n "const foodMeasures = " | cat - data/processed/measures.json > data/processed/measures_def.js
printf "\nmodule.exports = foodMeasures\n" >> data/processed/measures_def.js
```

## 6. Copy everything for use in Ingreedy

```bash
cp data/processed/*_def.js ../ingreedy-js/src
```