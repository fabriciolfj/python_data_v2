import pandas_teste as pd
import numpy as np

s1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

s2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'g'])


print(s2 + s1)


df1 = pd.DataFrame(np.arange(9).reshape((3, 3)), columns=list("bcd"), index=["ohio", "texas", "colorado"])

df2 = pd.DataFrame(np.arange(9).reshape((3, 3)), columns=list("bde"), index=["ohio", "texas", "oregon"])


print(df1 + df2)


df3 = df1 + df2
df3.fillna(0, inplace=True) #substitui NaN por 0
print(df3)