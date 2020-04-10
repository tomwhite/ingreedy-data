import pandas as pd
import sys

# Mapping from group code to name for the McCance dataset
group_codes = {
    'A': 'Cereals',
    'B': 'Milk',
    'C': 'Eggs',
    'D': 'Vegetables',
    'F': 'Fruit',
    'G': 'Nuts and seeds',
    'H': 'Herbs and spices',
    'IF': 'Baby foods',
    'J': 'Fish',
    'M': 'Meat',
    'O': 'Fats and oils',
    'P': 'Beverages',
    'Q': 'Alcohol',
    'S': 'Sugars and snacks',
    'W': 'Soups, sauces, and misc'
}

def load_mccance():
    """Load the McCance dataset with the nutrients columns we are interested in, plus groups."""
    foods = pd.read_csv("data/raw/McCance___Widdowson_s_Composition_of_Foods_Integrated_Dataset.csv", skiprows=[1, 2])

    # rename and drop columns
    foods = foods.rename(columns={
        'Food Code': 'food_code',
        'Food Name': 'name',
        'Description': 'description',
        'Group': 'group',
        'Protein (g)': 'protein',
        'Fat (g)': 'fat',
        'Carbohydrate (g)': 'carbs',
        'Energy (kcal) (kcal)': 'cals',
        'AOAC fibre (g)': 'fibre'
    })
    foods = foods[['food_code', 'name', 'group', 'protein', 'fat', 'carbs', 'cals', 'fibre', 'description']]

    # replace N and Tr with 0
    foods = foods.replace('N', 0)
    foods = foods.replace('Tr', 0)

    # make columns numeric
    foods[['cals', 'carbs', 'fat', 'fibre', 'protein']] = foods[['cals', 'carbs', 'fat', 'fibre', 'protein']].apply(pd.to_numeric)

    # drop rows that have NaN in any of the nutrients columns we are interested in (but not fibre, since it is sparsely populated)
    #foods = foods.dropna(subset = ['cals', 'carbs', 'fat', 'protein'])

    # data fixes
    foods.loc[foods['name'] == 'Lemon juice, fresh', 'group'] = 'FC' # fruit juice (FC), not general juice (PE)

    # restrict the number of groups by taking the first letter, for a coarser categorization
    foods['g'] = foods['group'].apply(lambda x: x[0])
    foods['g2'] = foods['group'].apply(lambda x: group_codes[x[0]])

    return foods
