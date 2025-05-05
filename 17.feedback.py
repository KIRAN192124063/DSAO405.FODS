import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = [word for word in text.split() if word not in stop_words]
    return words

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        if 'feedback' not in df.columns:
            raise ValueError("CSV must contain a column named 'feedback'")
        return df['feedback'].dropna()
    except Exception as e:
        print(f"Error loading file: {e}")
        return []

def analyze_feedback(file_path, top_n):
    feedback_series = load_dataset(file_path)
    all_words = []

    for feedback in feedback_series:
        words = preprocess_text(feedback)
        all_words.extend(words)

    word_freq = Counter(all_words)
    most_common = word_freq.most_common(top_n)

    print(f"\nTop {top_n} Most Frequent Words:")
    for word, freq in most_common:
        print(f"{word}: {freq}")

    words, frequencies = zip(*most_common)
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {top_n} Most Frequent Words in Customer Feedback')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if _name_ == "_main_":
    file_path = (r'C:\Users\91637\OneDrive\Desktop\sev\feedback.csv')
    try:
        top_n = int(input("Enter the number of top frequent words to display: "))
        analyze_feedback(file_path, top_n)
    except ValueError:
        print("Please enter a valid number.")
