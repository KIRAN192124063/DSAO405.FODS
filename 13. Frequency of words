import string
from collections import Counter
def count_word_frequency(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()  
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    
   
    words = text.split()
    
   
    word_count = Counter(words)
    
   
    for word, count in word_count.items():
        print(f'{word}: {count}')

count_word_frequency("story.txt")
