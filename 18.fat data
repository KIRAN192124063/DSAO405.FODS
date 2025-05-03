import pandas as pd
data = {
    "Age": [23, 25, 30, 32, 40, 41, 45, 50, 52, 55, 60, 62, 65, 68, 70, 72, 75, 80],
    "%Fat": [12, 15, 18, 20, 22, 24, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
}

df = pd.DataFrame(data)
mean_age = df["Age"].mean()
median_age = df["Age"].median()
std_age = df["Age"].std()

mean_fat = df["%Fat"].mean()
median_fat = df["%Fat"].median()
std_fat = df["%Fat"].std()

print(f"Mean Age: {mean_age}, Median Age: {median_age}, Standard Deviation of Age: {std_age}")
print(f"Mean %Fat: {mean_fat}, Median %Fat: {median_fat}, Standard Deviation of %Fat: {std_fat}")
