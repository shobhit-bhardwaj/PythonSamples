'''
@author: Shobhit Bhardwaj
'''

import numpy as np

arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])
print(arr_2d)
print(arr_2d[0][1])
print(arr_2d[1,2])
print(arr_2d[:2,1:])

arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)
print(arr_2d[1:3,3:5])