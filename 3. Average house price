import numpy as np
import pandas as pd 

house_data = np.array([
    [3, 1800, 250000],
    [4, 2200, 320000],
    [5, 2600, 400000],
    [6, 3000, 480000],
    [4, 2000, 310000],
    [5, 2800, 420000],
    [6, 3200, 500000],
    [3, 1500, 210000],
    [5, 2700, 390000],
    [4, 2300, 330000]
])

filtered_houses = house_data[house_data[:, 0] > 4]
average_price = np.mean(filtered_houses[:, 2])

print(f"The average sale price of houses with more than four bedrooms is: {average_price}")
