import pandas as pd
import numpy as np
from scipy.stats import t
file_path = "customer_reviews.csv" 
df = pd.read_csv(file_path)
ratings = df["rating"].dropna()  
sample_mean = np.mean(ratings)
sample_std = np.std(ratings, ddof=1)  
n = len(ratings)
confidence_level = 0.95
alpha = 1 - confidence_level
t_score = t.ppf(1 - alpha / 2, df=n - 1)
margin_error = t_score * (sample_std / np.sqrt(n))
lower_bound = sample_mean - margin_error
upper_bound = sample_mean + margin_error
print(f"Sample Mean Rating: {sample_mean:.2f}")
print(f"95% Confidence Interval: ({lower_bound:.2f}, {upper_bound:.2f})")
