#2. Write a Python program to get the largest and smallest number from a list without builtin functions.
def find_largest_smallest(numbers):
    """
    Find the largest and smallest numbers in a list.

    Parameters:
    numbers (list): A list of numeric elements.

    Returns:
    tuple: A tuple containing two elements:
           - The largest number in the list
           - The smallest number in the list
    """
    if not numbers:  # Check if the list is empty
        return None, None  # Return None for both largest and smallest
    
    # Initialize variables to store largest and smallest numbers
    largest = numbers[0]
    smallest = numbers[0]
    
    # Iterate through each number in the list
    for num in numbers:
        if num > largest:  # If current number is larger than 'largest'
            largest = num  # Update 'largest'
        elif num < smallest:  # If current number is smaller than 'smallest'
            smallest = num  # Update 'smallest'
    
    return largest, smallest  # Return the largest and smallest numbers

# Example usage:
my_numbers = [45, 67, 12, 89, 3, 27]
largest_num, smallest_num = find_largest_smallest(my_numbers)
print(f"The largest number is: {largest_num}")
print(f"The smallest number is: {smallest_num}")


"""
Output:

The largest number is: 89
The smallest number is: 3
"""

