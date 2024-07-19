#2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”


def count_words(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Initialize word count to zero
            word_count = 0
            # Iterate through each line in the file
            for line in file:
                # Split each line into words based on whitespace
                words = line.split()
                # Increment word count by the number of words in the line
                word_count += len(words)
            
            # Print the total word count
            print(f"Total number of words in '{filename}': {word_count}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read from file '{filename}'.")

# Example usage:
filename = 'ABC.txt'
count_words(filename)



"""
Output:
Total number of words in 'ABC.txt': 2
"""
