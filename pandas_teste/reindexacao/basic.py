# reorganiza os objetos com base no index informado
import pandas as pd
import numpy as np

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=["d", "b", "a", "c"])

print(obj)

obj2 = obj.reindex(["c", "b", "d", "a", "e"])
print(obj2)

obj3 = pd.Series(["blue", "purple", "yellow"], index=[0, 2, 4])
print(obj3)

print("===============")

obj3 = obj3.reindex(np.arange(6), method="ffill")
print(obj3)

print("=======Dataframe========")
print("===============")

frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=["a", "b", "c"], columns=["Ohio", "Texas", "California"])
print(frame)

#reorganizando as linhas
frame2 = frame.reindex(index=["a", "b", "c", "d", "e"])
print(frame2)

#reorganizando as colunas
frame2 = frame.reindex(columns=["Texas", "Utah", "California"])
print(frame2)

frame2 = pd.DataFrame(np.arange(9).reshape((3, 3)), index=["a", "b", "c"], columns=["Ohio", "Texas", "California"])

#usando loc para reorganizar, funciona se o index e a coluna ja existir no dataframe
frame2 = frame2.loc[["a", "b", "c"], ["Texas", "Ohio", "California"]]
print(frame2)

