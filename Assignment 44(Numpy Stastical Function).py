"""
2.Compute the standard deviation of the NumPy array

Input: arr = [20, 2, 7, 1, 34]
"""

# importing numpy as library
# numpy.std() method
import numpy as np
#1D array
arr = [20, 2, 7, 1, 34]
print("arr : ",  arr)
print("std of arr : ", np.std(arr))

print("\nMore precision with float32")
print("std of arr : ", np.std(arr, dtype= np.float32))

print("\nMore accuracy with float64")
print("std of arr : ", np.std(arr, dtype= np.float64))


"""
Output:
arr :  [20, 2, 7, 1, 34]
std of arr :  12.576167937809991

More precision with float32
std of arr :  12.576168

More accuracy with float64
std of arr :  12.576167937809991
"""
