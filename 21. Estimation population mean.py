import numpy as np
import pandas as pd
from scipy import stats

# Load data
data = pd.read_csv("rare_elements.csv")
concentrations = data.values.flatten()

# User input
n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level (e.g. 0.95): "))

# Random sample
sample = np.random.choice(concentrations, size=n, replace=False)
mean = np.mean(sample)
std_err = stats.sem(sample)
margin = std_err * stats.t.ppf((1 + confidence) / 2, df=n-1)

print(f"Sample Mean: {mean:.4f}")
print(f"{int(confidence*100)}% Confidence Interval: ({mean - margin:.4f}, {mean + margin:.4f})")
