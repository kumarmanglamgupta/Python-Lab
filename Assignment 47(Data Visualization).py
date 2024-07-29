"""
1. Install matplotlib  & you can use plt.plot() to create a line plot of given data

x = [0, 5, 9, 10, 15, 20, 25] 

y = [0, 1, 2, 3, 4, 5, 6]
"""


# Import the necessary library
import matplotlib.pyplot as plt

# Define the data for the plot
x = [0, 5, 9, 10, 15, 20, 25]
y = [0, 1, 2, 3, 4, 5, 6]

# Create a new figure for the plot
plt.figure()

# Plot the data: 'o' marker adds markers to the data points
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data Line')

# Add a title to the plot
plt.title('Line Plot of x vs. y')

# Label the x-axis
plt.xlabel('x values')

# Label the y-axis
plt.ylabel('y values')

# Add a legend to the plot
plt.legend()

# Display the plot
plt.show()
