import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "key1" : ["a", "a", None, "b", "b", "a", None],
        "key2" : pd.Series([1, 2, 1, 2, 1, None, 1], dtype="Int64"),
        "data1" : pd.Series([1, 2, 3, 4, 5, 6, 7], dtype="Int64"),
        "data2" : pd.Series([1, 2, 3, 4, 5, 6, 7], dtype="Int64")
    }
)

grouped = df.groupby("key1")
print(df)
print("=============")
#2 menores valores de cada grupo
print(grouped["data1"].nsmallest(2))

def peak_to_peak(arr):
    return arr.max() - arr.min()

print("=============")
print(grouped.agg(peak_to_peak))