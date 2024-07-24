"""
1.Compute the median of the flattened NumPy array 

Input: x_odd = np.array([1, 2, 3, 4, 5, 6, 7])
"""

# importing numpy as library
import numpy as np

# Input array
x_odd = np.array([1, 2, 3, 4, 5, 6, 7])
print("\nPrinting the original array:")
print(x_odd)

# Calculate the median
median = np.median(x_odd)
print ("\nMedian of the array that contains print odd no elements:")
# Output the result
print(median)



"""
Output:
Printing the original array:
[1 2 3 4 5 6 7]

Median of the array that contains print odd no elements:
4.0
"""
