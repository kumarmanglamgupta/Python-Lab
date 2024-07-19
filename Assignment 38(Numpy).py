#2. Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.

#Input: my_list = [1, 2, 3, 4, 5]



import numpy as np  # Importing NumPy with alias np

# Input list
my_list = [1, 2, 3, 4, 5]

# Convert list to NumPy array
my_array = np.array(my_list)

# Display the array
print("NumPy array:", my_array)

# Display the first and last index
first_index = 0
last_index = len(my_array) - 1
print(f"First index: {first_index}, value: {my_array[first_index]}")
print(f"Last index: {last_index}, value: {my_array[last_index]}")

# Multiply each element by 2
my_array *= 2

# Display the result after multiplication
print("Array after multiplying each element by 2:", my_array)



"""
Output:
NumPy array: [1 2 3 4 5]
First index: 0, value: 1
Last index: 4, value: 5
Array after multiplying each element by 2: [ 2  4  6  8 10]
"""
