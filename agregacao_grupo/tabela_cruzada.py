import pandas as pd


tips = pd.read_csv("../files/tips.csv")

tips["tip_pct"] = tips["tip"] / tips["total_bill"]

print(tips.pivot_table(index=["day", "smoker"], aggfunc="sum"))

print("=============calcular somente tip_pct, size")
print(tips.pivot_table(index=["time", "day"], columns="smoker", values=["tip_pct", "size"], margins=True))
print("========para calcular as frequencias")
print(pd.crosstab([tips["time"], tips["day"]], tips["smoker"], margins=True))