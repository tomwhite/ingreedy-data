# Take the NYT ingredient list dataset and do normalization on the names (that were tagged by humans).
# Then a human (me) can map these names to foods in a food database.
# This will be the basis for building a model that can map ingredient lines to nutrients.

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
import pandas as pd

#import nltk
#nltk.download('wordnet')

tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()
# Normalize the name
def normalize_name(name):
    n = name
    n = n.lower()
    tokens = tokenizer.tokenize(n)
    lemmas = [lemmatizer.lemmatize(w) for w in tokens]
    return ' '.join(lemmas)

df = pd.read_csv("data/raw/nyt-ingredients-snapshot-2015.csv")
df = df.drop_duplicates(['input', 'name'])
df = df[df['name'].notnull()]

# Remove diacritics
df['normalized_name'] = df['name'].str.normalize('NFKD')\
       .str.encode('ascii', errors='ignore')\
       .str.decode('utf-8')
df['normalized_name'] = df['normalized_name'].apply(normalize_name)
x = df.groupby('normalized_name').size().reset_index(name='counts').sort_values('counts', ascending=False)

x_10 = x[x['counts'] >= 10]
x_10.to_csv("data/processed/nyt_food_names.csv", index=False)
