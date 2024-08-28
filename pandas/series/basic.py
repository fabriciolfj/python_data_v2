import pandas as pd

obj = pd.Series([4, 7, -5, 3])

print(obj)

obj = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
obj2 = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])

print(obj)
obj['b'] = 6

print(obj)

print("b" in obj)


print(pd.isna(obj))

print(obj + obj2)