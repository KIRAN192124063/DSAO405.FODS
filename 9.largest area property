import pandas as pd
data = {
    'property_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'location': ['City A', 'City B', 'City A', 'City C', 'City B', 'City A', 'City C', 'City A', 'City B', 'City C'],
    'bedrooms': [3, 5, 2, 4, 6, 3, 3, 5, 4, 6],
    'area': [1500, 2200, 900, 1800, 2500, 1300, 1600, 2100, 1700, 3000],
    'listing_price': [400000, 600000, 350000, 500000, 750000, 380000, 450000, 650000, 480000, 800000]
}
property_data = pd.DataFrame(data)
avg_listing_price = property_data.groupby('location')['listing_price'].mean()
num_properties_more_than_four_bedrooms = property_data[property_data['bedrooms'] > 4].shape[0]
property_with_largest_area = property_data.loc[property_data['area'].idxmax()]
print("1. Average listing price of properties in each location:")
print(avg_listing_price)
print("\n2. Number of properties with more than four bedrooms:", num_properties_more_than_four_bedrooms)
print("\n3. Property with the largest area:")
print(property_with_largest_area)
