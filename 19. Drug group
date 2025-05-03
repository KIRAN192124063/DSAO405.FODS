import numpy as np
import scipy.stats as stats

drug_group = [10, 12, 15, 14, 17, 19, 21, 18, 20, 22, 23, 25, 26, 28, 30, 32, 34, 35, 37, 40, 42, 44, 46, 48, 50]
placebo_group = [5, 6, 8, 7, 10, 11, 12, 9, 13, 15, 16, 17, 18, 20, 22, 23, 24, 26, 27, 30, 32, 33, 35, 37, 38]
mean_drug = np.mean(drug_group)
std_drug = np.std(drug_group, ddof=1)
n_drug = len(drug_group)
mean_placebo = np.mean(placebo_group)
std_placebo = np.std(placebo_group, ddof=1)
n_placebo = len(placebo_group)
t_value_drug = stats.t.ppf(0.975, df=n_drug-1)
t_value_placebo = stats.t.ppf(0.975, df=n_placebo-1)
margin_error_drug = t_value_drug * (std_drug / np.sqrt(n_drug))
margin_error_placebo = t_value_placebo * (std_placebo / np.sqrt(n_placebo))

ci_drug = (mean_drug - margin_error_drug, mean_drug + margin_error_drug)
ci_placebo = (mean_placebo - margin_error_placebo, mean_placebo + margin_error_placebo)

print(f"95% Confidence Interval for Drug Group: {ci_drug}")
print(f"95% Confidence Interval for Placebo Group: {ci_placebo}")
