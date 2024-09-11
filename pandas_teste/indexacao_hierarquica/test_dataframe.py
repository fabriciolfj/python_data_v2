import pandas as pd
import numpy as np


frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[["a", "a", "b", "b"], [1, 2, 1, 2]],
                     columns=[["Ohio", "Ohio", "Colorado"], ["Green", "Red", "Green"]])
frame.index.names = ["key1", "key2"]
frame.columns.names = ["state", "color"]
print(frame["Ohio"])

#trocando de niveis
print("==================")
frame = frame.swaplevel("key1", "key2")
print(frame)
#ordenando pelo index mais externo
print("==================")
frame = frame.sort_index(level=0)
print(frame)
#somando e agrupando
print("==================")
print(frame.groupby(level="key2").sum())
print("==================")
#por colunas
print(frame.T.groupby(level="color").sum().T)