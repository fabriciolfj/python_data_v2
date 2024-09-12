import pandas as pd
import numpy as np


df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=["a", "b", "c"], columns=["one", "two"])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=["a", "c"], columns=["three", "four"])

#colocando uma hierarquia com base na coluna
result = pd.concat([df1, df2], axis="columns", keys=["level1", "level2"])
#da o mesmo resultado
result = pd.concat({"level1" : df1, "level2" : df2}, axis="columns", names=["upper", "owner"])
print(result)
print("=================")
result = pd.concat([df1, df2], keys=["level1", "level2"])
print(result)