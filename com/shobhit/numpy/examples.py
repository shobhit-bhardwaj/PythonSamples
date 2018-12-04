'''
@author: Shobhit Bhardwaj
'''

import numpy as np

# Array of Zeros
arr = np.zeros(5)
print(arr)


# Array of Ones
arr = np.ones(5)
print(arr)


# Array of 5's
arr = np.zeros(5) + 5
arr = np.ones(5) * 5
print(arr)


# Array of Integers from 10 to 50
arr = np.arange(10, 51)
print(arr)


# Array of Even Integers from 10 to 50
arr = np.arange(10, 51, 2)
print(arr)


# 3x3 Matrix of 0 to 8
arr = np.arange(9).reshape(3,3)
print(arr)


# 3x3 Identity Matrix
arr = np.eye(3,3)
print(arr)


# Generate random number from 0 to 1
random = np.random.rand(1)
print(random)


# Print 25 Random Numbers (Standard Normal Distribution)
arr = np.random.randn(25)
print(arr)
