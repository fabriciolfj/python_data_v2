import pandas as pd

data = pd.DataFrame(
    {"k1" : ["one", "two"] * 3 + ["two"],
     "k2" : [1, 1, 2, 3, 3, 4, 4]}
)

print(data)
print("==================")
print(data.duplicated())
print("==================")
print(data.drop_duplicates())
print("==================")
#levando em consideracao apenas a coluna k1
print(data.drop_duplicates(subset=["k1"]))