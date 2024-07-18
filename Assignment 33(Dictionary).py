#1. Write a Python program and calculate the mean of the below dictionary.

#test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}

def calculate_mean(dictionary):
    """
    Calculate the mean (average) of values in a dictionary.

    Parameters:
    dictionary (dict): A dictionary where values are numeric.

    Returns:
    float: The mean of values in the dictionary.
    """
    if not dictionary:  # Check if the dictionary is empty
        return 0.0  # Return 0.0 if dictionary is empty
    
    total_sum = 0
    count = 0
    
    # Iterate through each value in the dictionary
    for value in dictionary.values():
        total_sum += value  # Add each value to the total sum
        count += 1  # Increment count to keep track of number of elements
    
    mean = total_sum / count  # Calculate the mean
    
    return mean

# Given dictionary
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Calculate the mean
mean_value = calculate_mean(test_dict)

# Print the output
print(f"The mean of the dictionary values is: {mean_value}")



"""
Output:
The mean of the dictionary values is: 6.2
"""
