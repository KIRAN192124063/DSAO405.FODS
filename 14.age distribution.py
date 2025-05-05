import pandas as pd
import matplotlib.pyplot as plt
data = {'Customer_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Age': [25, 30, 22, 40, 35, 30, 25, 40, 50, 35]}

df = pd.DataFrame(data)
age_distribution = df['Age'].value_counts().sort_index()
print(age_distribution)
plt.bar(age_distribution.index, age_distribution.values)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Frequency Distribution of Customer Ages')
plt.show()
