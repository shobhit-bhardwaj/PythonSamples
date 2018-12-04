'''
@author: Shobhit Bhardwaj
'''

import numpy as np

arr = np.arange(0, 11);
print(arr)

print(arr[5])
print(arr[2:5])
print(arr[:6])
print(arr[3:])

arr[2:5] = 100
print(arr)

arr = np.arange(0, 11)
print(arr)

arr_slice = arr[2:6]
print(arr_slice)
arr_slice[:] = 99
print(arr_slice)
print(arr)

arr_copy = arr.copy()
arr_copy[:] = 100
print(arr_copy)
print(arr)

arr = np.arange(0, 11)
print(arr)
bool_array = arr > 5
print(bool_array)
print(arr[bool_array])
print(arr[arr>5])
