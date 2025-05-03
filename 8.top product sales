import pandas as pd
import numpy as np
data = {
    'product_name': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Headphones', 'Phone', 'Laptop', 'Headphones'],
    'order_date': ['2024-03-01', '2024-03-02', '2024-03-05', '2024-03-10', '2024-03-12', '2024-03-15', '2024-03-18', '2024-03-20', '2024-03-25', '2024-03-28'],
    'order_quantity': [5, 10, 3, 7, 8, 4, 2, 6, 1, 3]
}
sales_data = pd.DataFrame(data)

sales_data['order_date'] = pd.to_datetime(sales_data['order_date'])

start_date = pd.to_datetime('2024-03-01')
end_date = pd.to_datetime('2024-03-31')

recent_sales_data = sales_data[(sales_data['order_date'] >= start_date) & (sales_data['order_date'] <= end_date)]

print("\nFiltered sales data (March 2024):")
print(recent_sales_data)

product_sales = recent_sales_data.groupby('product_name')['order_quantity'].sum()

top_5_products = product_sales.sort_values(ascending=False).head(5)

print("\nTop 5 products sold the most in March 2024:")
print(top_5_products)
