'''
@author: Shobhit Bhardwaj
'''

import numpy as np
import pandas as pd

dict = {'A': [1, 2, np.nan], 'B': [3, np.nan, np.nan], 'C': [1, 2, 3]}

df = pd.DataFrame(dict)
print(df)

print(df.dropna())
print(df.dropna(axis=1))

print(df.dropna(thresh=2))
print(df.dropna(axis=1, thresh=2))

print(df.fillna(value='FILL VALUE'))

df['A'].fillna(value=df['A'].mean(), inplace=True)
print(df)
