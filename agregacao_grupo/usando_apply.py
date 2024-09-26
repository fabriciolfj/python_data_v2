import pandas as pd
from sqlalchemy import column

tips = pd.read_csv("../files/tips.csv")

tips["tip_pct"] = tips["tip"] / tips["total_bill"]

def top(df, n=5, column="tip_pct"):
    return df.nlargest(n, columns=column)

print(tips.groupby("smoker").apply(top))
print("=================")
print(tips.groupby(["smoker", "day"], group_keys=False).apply(top, column="total_bill"))
print("=================")
print(tips.groupby("smoker")["tip_pct"].describe())