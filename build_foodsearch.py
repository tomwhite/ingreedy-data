# Export McCance as a cleaned-up CSV and JSON

from mccance import load_mccance

if __name__ == '__main__':
    foods = load_mccance()
    foods.to_csv('data/processed/McCance_minimal.csv', index=False)
    foods.to_json('data/processed/foodsearch.json', orient='records')
