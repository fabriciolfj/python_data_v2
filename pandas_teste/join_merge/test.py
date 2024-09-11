import pandas as pd

df1 = pd.DataFrame(
    {
        "key": ["b", "b", "a", "c", "a", "a", "b"],
        "data": pd.Series(range(7), dtype="Int64")
    }
)

df2 = pd.DataFrame(
    {
        "key": ["a", "b", "d"],
        "data": pd.Series(range(3), dtype="Int64")
    }
)

print(df1)
print("============")
print(df2)
#merge por default e similar ao join, somente aonde der match
print(pd.merge(df2, df1, on="key", suffixes=("_left", "_right"), indicator=True))

df3 = pd.DataFrame(
    {
        "lkey": ["b", "b", "a", "c", "a", "a", "b"],
        "data1": pd.Series(range(7), dtype="Int64")
    }
)

df4 = pd.DataFrame(
    {
        "rkey": ["a", "b", "d"],
        "data2": pd.Series(range(3), dtype="Int64")
    }
)

print("============")
#se os nomes forem diferentes aonde queremos fazer o join
print(pd.merge(df3, df4, left_on="lkey", right_on="rkey"))

print("============")
#aonde nao encontrar em um fica como NA
print(pd.merge(df2, df1, how="outer"))


print("============")
#default inner
print(pd.merge(df2, df1, how="inner"))

print("============")
#olha o que tem na esquerda, o da direita der match mostra se nao n/a
print(pd.merge(df2, df1, how="left", on="key", suffixes=("_left", "_right"), indicator=True))

print("============")
#olha o que tem na direita, o da esquerda der match mostra se nao n/a
print(pd.merge(df2, df1, how="right", on="key", suffixes=("_left", "_right"), indicator=True))