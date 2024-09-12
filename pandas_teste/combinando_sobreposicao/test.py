import pandas as pd
import numpy as np

a = pd.Series([np.nan, 2.5, 0.0, 3.5, 4.5, np.nan], index=["f", "e", "d", "c", "b", "a"])
b = pd.Series([0., np.nan, 2.0, np.nan, np.nan, 5.0], index=["a", "b", "c", "d", "e", "f"])
#aonde for nulo, uso valor de b
result = a.combine_first(b)
print(result)
#com dataframe
df1 = pd.DataFrame({
    "a" : [1., np.nan, 5., np.nan],
    "b" : [np.nan, 2., np.nan, 6.],
    "c" : range(2, 18, 4),
})

df2 = pd.DataFrame({
    "a" : [5., 4, np.nan, 3., 7.],
    "b" : [np.nan, 3., 4., 6., 8.]
})

print("===============")
print(df1.combine_first(df2))