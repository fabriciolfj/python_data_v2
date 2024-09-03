import pandas_teste as pd

chunker = pd.read_csv("ex6.csv", chunksize=1000)

tot = pd.Series([], dtype='int64')

for piece in chunker:
    print(piece)
    tot = tot.add(piece["key"].value_counts(), fill_value=0)

tot = tot.sort_values(ascending=False)

print("==========")
print(tot)