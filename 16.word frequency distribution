import pandas as pd
from collections import Counter
import re
df = pd.read_csv(r"C:\Users\sjsur\reviews.csv")

all_reviews = ' '.join(df['review'].dropna().astype(str))

words = re.findall(r'\b\w+\b', all_reviews.lower())  

word_freq = Counter(words)

print("Word Frequency Distribution:")
for word, freq in word_freq.most_common():
    print(f"{word}: {freq}")
