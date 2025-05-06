import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

np.random.seed(42)

control_group = np.random.normal(loc=50, scale=10, size=100)  # mean = 50, std = 10

treatment_group = np.random.normal(loc=55, scale=10, size=100)  # mean = 55, std = 10

t_stat, p_value = stats.ttest_ind(control_group, treatment_group)

plt.figure(figsize=(10, 6))

plt.hist(control_group, bins=20, alpha=0.7, label='Control Group (Placebo)', color='blue')
plt.hist(treatment_group, bins=20, alpha=0.7, label='Treatment Group (New Drug)', color='orange')

plt.title('Distribution of Scores: Control Group vs Treatment Group')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.legend()

plt.figtext(0.15, 0.85, f'p-value = {p_value:.4f}', fontsize=12, color='red')

plt.show()
if p_value < 0.05:
    print(f"Statistically significant result! (p-value = {p_value:.4f})")
else:
    print(f"No statistically significant difference (p-value = {p_value:.4f})")
