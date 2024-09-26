import pandas as pd
import numpy as np

df = pd.DataFrame({
    "data1" : np.random.standard_normal(1000),
    "data2" : np.random.standard_normal(1000)
})

print(df)

quartiles = pd.cut(df["data1"], 4)
grouped = df.groupby(quartiles)

print(grouped.agg(["sum", "mean", "max", "min"])["data1"])
