'''
@author: Shobhit Bhardwaj
'''

import numpy as np

arr = np.random.rand(2)
print(arr)

arr = np.random.rand(3,3)
print(arr)

arr = np.random.randn(3)
print(arr)

arr = np.random.randn(2,2)
print(arr)

arr = np.random.randint(1,25)
print(arr)

arr = np.random.randint(1,25,5)
print(arr)

arr = np.random.randint(1,25,(5,3))
print(arr)

arr = np.arange(0,25)
print(arr)
arr = arr.reshape(5,5)
print(arr)

arr = np.random.randint(1,50,10)
print(arr)
print(arr.shape)
print(arr.dtype)

print(arr.argmax())
print(arr.max())
print(arr.argmin())
print(arr.min())
