#1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.


def read_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read each line in the file
            for line in file:
                # Print each line to the screen
                print(line, end='')  # 'end='' is used to avoid double spacing due to print() adding a newline by default
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read from file '{filename}'.")

# Example usage:
filename = 'ABC.txt'
read_file(filename)


"""
Output:
Hello World
"""
