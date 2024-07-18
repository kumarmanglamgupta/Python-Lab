# 2.Write a Python script to concatenate the following dictionaries to create a new one. 

#Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60}

def concatenate_dicts(*dicts):
    """
    Concatenate multiple dictionaries into a new dictionary.

    Parameters:
    *dicts (dict): Variable length argument list of dictionaries.

    Returns:
    dict: A new dictionary containing all key-value pairs from input dictionaries.
    """
    concatenated_dict = {}  # Initialize an empty dictionary to store the concatenated result
    
    for dictionary in dicts:  # Iterate through each dictionary in the input
        concatenated_dict.update(dictionary)  # Update the concatenated_dict with key-value pairs from current dictionary
    
    return concatenated_dict

# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate dictionaries
result_dict = concatenate_dicts(dic1, dic2, dic3)

# Print the result
print("Concatenated Dictionary:", result_dict)



"""
Output:
Concatenated Dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
