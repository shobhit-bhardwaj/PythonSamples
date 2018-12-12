'''
@author: Shobhit Bhardwaj
'''

import numpy as np
import pandas as pd

data = {'Company':['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'], 'Person':['Sam', 'Cherry', 'Brooks', 'Tom', 'Jane', 'Andrew'], 'Sales':[200, 120, 150, 340, 240, 180]}

df = pd.DataFrame(data)
print(df)

byCompany = df.groupby('Company')
print(byCompany.count())
print(byCompany.sum())
print(byCompany.mean())
print(byCompany.std())
print(df.groupby('Company').count().loc['FB'])
print(df.groupby('Sales').min())
print(df.groupby('Company').describe().transpose())
