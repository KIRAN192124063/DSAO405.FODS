import matplotlib.pyplot as plt

days = list(range(1, 31))
sales = [100 + i * 5 for i in range(30)]  
plt.plot(days, sales, marker='o', linestyle='-')
plt.xlabel('Day of the Month')
plt.ylabel('Sales')
plt.title('Sales Trend Over a Month')
plt.grid()
plt.show()
days = list(range(1, 31))
sales = [100 + (i * 5 + (-1)**i * 15) for i in range(30)] 
plt.scatter(days, sales, color='red')
plt.xlabel('Day of the Month')
plt.ylabel('Sales')
plt.title('Sales Distribution Over a Month')
plt.grid()
plt.show()
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1200, 1500, 1800, 1600, 2000, 2200, 2100, 2500, 2400, 2600, 2800, 3000]

plt.bar(months, sales, color='blue')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Data')
plt.xticks(rotation=45)
plt.show()
