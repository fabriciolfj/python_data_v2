import pandas as pd

df = pd.DataFrame(
    {
        "key1" : ["a", "a", None, "b", "b", "a", None],
        "key2" : pd.Series([1, 2, 1, 2, 1, None, 1], dtype="Int64"),
        "data1" : pd.Series([1, 2, 3, 4, 5, 6, 7], dtype="Int64"),
        "data2" : pd.Series([1, 2, 3, 4, 5, 6, 7], dtype="Int64")
    }
)

for name, group in df.groupby("key1"):
    print(name)
    print(group)

print("==============")

for (k1, k2), group in df.groupby(["key1", "key2"]):
    print((k1, k2))
    print(group)

print("========")
print(df)

print("==========")
grouped = df.groupby(
    {
        "key1" :"key", "key2" : "key",
        "data1" : "data", "data2" : "data"
    }, axis="columns"
)

for group_key, group_values in grouped:
    print(group_key)
    print(group_values)

print("============")
print(df.groupby(["key1", "key2"])[["data2"]].mean())