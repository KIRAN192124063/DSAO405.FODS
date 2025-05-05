import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [10000, 15000, 20000, 18000, 22000, 25000, 23000, 27000, 26000, 29000, 32000, 34000]
plt.figure(figsize=(10, 6))  # Set the size of the plot
plt.plot(months, sales, marker='o', color='b', linestyle='-', linewidth=2, markersize=8)
plt.title('Monthly Sales (Line Plot)', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.grid(True)  
plt.show()
plt.figure(figsize=(10, 6))  # Set the size of the plot
plt.bar(months, sales, color='g')
plt.title('Monthly Sales (Bar Plot)', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.show()
