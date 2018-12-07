'''
@author: Shobhit Bhardwaj
'''

import numpy as np
import pandas as pd

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]

combine = list(zip(outside, inside))
print(combine)

hier_index = pd.MultiIndex.from_tuples(combine)
print(hier_index)

df = pd.DataFrame(np.random.randn(6,2), hier_index, ['A', 'B'])
print(df)

print(df.loc['G1'])
print(df.loc['G1'].loc[2]['B'])

df.index.names = ['Groups', 'Numbers']
print(df)

print(df.xs('G1'))
print(df.xs(1, level = 'Numbers'))
