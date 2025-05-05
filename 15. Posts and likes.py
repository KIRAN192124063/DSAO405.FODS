import pandas as pd
import matplotlib.pyplot as plt

data = {'Post_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Likes': [50, 75, 50, 100, 150, 75, 100, 50, 200, 150]}

df = pd.DataFrame(data)

like_distribution = df['Likes'].value_counts().sort_index()
print(like_distribution)
plt.bar(like_distribution.index, like_distribution.values)
plt.xlabel('Number of Likes')
plt.ylabel('Frequency')
plt.title('Frequency Distribution of Likes Among Posts')
plt.show()
