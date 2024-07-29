"""
1. Calculate the total revenue generated by two product categories in a store 

Input: category1_revenue = np.array([500, 600, 700, 550]) 

category2_revenue = np.array([450, 700, 800, 600]) 

Output: Total Revenue: [ 950 1300 1500 1150] 
"""


# Import the NumPy library
import numpy as np

# Define the revenue for the two product categories
category1_revenue = np.array([500, 600, 700, 550])
category2_revenue = np.array([450, 700, 800, 600])

# Calculate the total revenue by summing the two arrays element-wise
total_revenue = category1_revenue + category2_revenue

# Print the result
print("Total Revenue:", total_revenue)




"""
Output:
Total Revenue: [ 950 1300 1500 1150]
"""