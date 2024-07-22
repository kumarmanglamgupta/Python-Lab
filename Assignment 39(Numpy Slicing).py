#1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

import numpy as np

# Create an array of 10 zeros
array_zeros = np.zeros(10)

# Create an array of 10 ones
array_ones = np.ones(10)

# Create an array of 10 fives
array_fives = np.ones(10) * 5

# Concatenate arrays to get the final array
final_array = np.concatenate([array_zeros, array_ones, array_fives])

print("Array of 10 zeros:")
print(array_zeros)

print("\nArray of 10 ones:")
print(array_ones)

print("\nArray of 10 fives:")
print(array_fives)

print("\nFinal concatenated array:")
print(final_array)


"""
Output:
Array of 10 zeros:
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

Array of 10 ones:
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

Array of 10 fives:
[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]

Final concatenated array:
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 5. 5. 5. 5. 5.
 5. 5. 5. 5. 5.]
"""
