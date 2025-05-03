import pandas as pd

order_data = pd.read_csv(r"C:\Apps\e commerce.csv")

order_data['order_date'] = pd.to_datetime(order_data['order_date'])

total_orders_per_customer = order_data.groupby('customer_id')['order_date'].count()

average_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()

earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()

print("\nTotal number of orders made by each customer:")
print(total_orders_per_customer)

print("\nAverage order quantity for each product:")
print(average_quantity_per_product)

print("\nEarliest order date in the dataset:", earliest_order_date)
print("Latest order date in the dataset:", latest_order_date)
