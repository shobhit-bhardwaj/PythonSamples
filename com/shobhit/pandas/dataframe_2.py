'''
@author: Shobhit Bhardwaj
'''

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

print(df > 0)
print(df[df>0])

print(df[df['Z']>0])
print(df[(df['W']>0) & (df['X']<0)])
print(df[(df['W']>0) | (df['X']<0)])

print(df.reset_index(inplace=True))

states = "RJ UP HR GJ DL".split()
df['states'] = states
print(df)

df.set_index('states', inplace = True)
print(df)
