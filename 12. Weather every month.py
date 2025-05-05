import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [15, 17, 22, 28, 32, 35, 34, 33, 30, 25, 20, 16]

plt.plot(months, temperature, marker='o', linestyle='-', color='blue')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature Variation')
plt.grid()
plt.xticks(rotation=45)
plt.show()
rainfall = [120, 100, 80, 60, 40, 30, 25, 35, 50, 90, 110, 130]

plt.scatter(months, rainfall, color='green')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall Distribution')
plt.grid()
plt.xticks(rotation=45)
plt.show()
