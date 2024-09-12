import pandas as pd

s1 = pd.Series([0, 1], index=["a", "b"], dtype="Int64")
s2 = pd.Series([2, 3, 4], index=["c", "d", "e"], dtype="Int64")
s3 = pd.Series([5, 6], index=["f", "g"], dtype="Int64")
s4 = pd.concat([s1, s3])

result = pd.concat([s1, s2, s3])
print(result)
#com colunas resulta em um dataframe usando how outer
print("===========")
result = pd.concat([s1, s2, s3], axis="columns")
print(result)
print("===========")
result = pd.concat([s1, s4], axis="columns", join="inner")
print(result)