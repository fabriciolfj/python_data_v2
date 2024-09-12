import pandas as pd

left1 = pd.DataFrame(
    {
        "key": ["a", "b", "c", "a", "b", "c"],
        "value": pd.Series(range(6), dtype="int64")
    }
)

right1 = pd.DataFrame({ "group_val" : [3.5, 7] }, index=["a", "b"])

print(left1)
print("==============")
print(right1)
print("left_on=key, right_index=True==============")
result = pd.merge(left1, right1, left_on="key", right_index=True)
print(result)
print("left_index=True, right_on=key==============")
result = pd.merge(right1, left1, left_index=True, right_on="key")
print(result)
print("left1.join(right1, on=key)==============")
#uso do join, ele faz a juncao a esquerda
result = left1.join(right1, on="key", how="inner")
print(result)