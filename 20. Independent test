import numpy as np
import scipy.stats as stats

design_A = [0.12, 0.15, 0.13, 0.11, 0.14, 0.16, 0.17, 0.14, 0.15, 0.13, 0.18, 0.19, 0.20, 0.21, 0.22]
design_B = [0.10, 0.12, 0.11, 0.09, 0.13, 0.12, 0.14, 0.13, 0.11, 0.12, 0.15, 0.16, 0.18, 0.17, 0.19]
mean_A = np.mean(design_A)
mean_B = np.mean(design_B)
t_stat, p_value = stats.ttest_ind(design_A, design_B, equal_var=False)

alpha = 0.05 
if p_value < alpha:
    print(f"The difference is statistically significant (p = {p_value:.4f}). Design A and B likely have different conversion rates.")
else:
    print(f"No statistically significant difference (p = {p_value:.4f}). The conversion rates are likely similar.")
