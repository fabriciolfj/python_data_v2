import pandas as pd
import numpy as np


obj = pd.Series([1, 2, 3], index=['a', 'b', 'c'])


obj = obj.drop(index=['a', 'c'])

print(obj)


data = pd.DataFrame(np.arange(16).reshape((4, 4)),index=['ohio', 'colorado', 'utah', 'new york'], columns=['A', 'B', 'C', 'D'])
print(data)

print("========")

data = data.drop(columns=['A', 'D'])
print(data)
print("========")

data = data.drop(index=['colorado'])
print(data)