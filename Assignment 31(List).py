#1. Write a Python program to sum all the items in a list.
def sum_of_list(items):
    """
    Calculate the sum of all the elements in a list.

    Parameters:
    items (list): A list containing numeric elements.

    Returns:
    int or float: The sum of all elements in the list.
    """
    total = 0  # Initialize a variable to store the sum, starting with 0
    
    # Iterate through each element in the list
    for item in items:
        total += item  # Add each element to the total
    
    return total  # Return the sum

# Example usage:
my_list = [10, 20, 30, 40, 50]
result = sum_of_list(my_list)
print(f"The sum of all elements in the list is: {result}")



"""
Output:
The sum of all elements in the list is: 150
"""
