'''
@author: Shobhit Bhardwaj
'''

import numpy as np
import pandas as pd

my_index = ['a','b','c']
my_data = [1,2,3]

ser = pd.Series(data=my_data, index=my_index)
print(ser)
ser = pd.Series(my_data, index=my_index)
print(ser)
ser = pd.Series(['India', 'Japan', 'France'])
print(ser)


my_map = {'a':1, 'b':'2', 'c':'3', 'd':'4', 'e':'5'}
ser = pd.Series(my_map)
print(ser)


map1 = {'USA':1, 'INDIA':2, 'FRANCE':3, 'JAPAN':4}
map2 = {'USA':1, 'INDIA':2, 'FRANCE':3, 'ITELY':5}

ser1 = pd.Series(map1)
ser2 = pd.Series(map2)

print(ser1 + ser2)
print(ser1 - ser2)
