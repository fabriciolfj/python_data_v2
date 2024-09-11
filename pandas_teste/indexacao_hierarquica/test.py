import pandas as pd
import numpy as np

data = pd.Series(np.random.uniform(size=9),
                 index=[["a", "a", "a", "b", "b", "b", "c", "c", "c"],
                        [1, 2, 3, 1, 2, 3, 1, 2, 3]])

print(data.index)
print("===================")
print(data['b'])
print("===================")
print(data['b':'c'])
print("===================")
print(data.loc[["b", "c"], 1])
print("===================")
print(data.loc[:, 2])

