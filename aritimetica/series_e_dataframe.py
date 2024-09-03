import pandas_teste as pd
import numpy as np

frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list("bde"), index=["utah", "ohio", "texas", "oregon"])

series = frame.iloc[0]

print(frame)

print("=============")

print(series)

#subtrai passando linha a linha
print("====================")
print(frame - series)

series3 = frame["d"]
print(series3)

#passando coluna a coluna, aonde da match do index com a coluna
result = frame.sub(series3, axis="index")
print(result)

