import pandas_teste as pd
import numpy as np

obj = pd.Series(np.arange(4), index=["d", "a", "b", "c"])


obj.sort_index()

print(obj)


frame = pd.DataFrame(np.arange(8).reshape((2, 4)), index=["three", "one"],
                     columns=["d", "a", "b", "c"])


print(frame.sort_index())

print(frame.sort_index(axis="columns"))


s = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(s.rank())


#verificando se tem duplicidade
print(obj.index.is_unique)