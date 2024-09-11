import pandas as pd
import numpy as np

left = pd.DataFrame({
    "key1" : ["foo", "foo", "bar"],
    "key2" : ["one", "two", "one"],
    "lval" : pd.Series([1, 2, 3], dtype="int64")
})

right = pd.DataFrame({
    "key1" : ["foo", "foo", "bar", "bar"],
    "key2" : ["one", "one", "one", "two"],
    "rval" : pd.Series([4, 5, 6, 7], dtype="int64")
})


print(pd.merge(left, right, on=["key1", "key2"], how="outer"))