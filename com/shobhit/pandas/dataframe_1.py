'''
@author: Shobhit Bhardwaj
'''

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)
print(df['W'])
print(df[['W',"X"]])

df['NEW'] = df['Y'] + df['Z']
print(df)

df.drop('NEW', axis=1, inplace=True)
print(df)

print(df.loc['B'])
print(df.iloc[1])

print(df.loc[['B','C','D']])
print(df.loc['B','Y'])

print(df.loc[['A','B'],['W','X']])
