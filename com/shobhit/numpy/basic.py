'''
@author: Shobhit Bhardwaj
'''

import numpy as np

my_list = [1,2,3]
arr = np.array(my_list)
print(arr)

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

arr = np.arange(0,10)
print(arr)

arr = np.arange(1,11,2)
print(arr)

arr = np.zeros(5)
print(arr)

arr = np.zeros((3,3))
print(arr)

arr = np.ones(5)
print(arr)

arr = np.ones((3,3))
print(arr)

arr = np.linspace(0,10,5)
print(arr)

arr = np.eye(4)
print(arr)
