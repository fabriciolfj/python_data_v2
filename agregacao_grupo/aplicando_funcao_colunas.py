import pandas as pd
import numpy as np


tips = pd.read_csv("../files/tips.csv")

tips["tip_pct"] = tips["tip"] / tips["total_bill"]


grouped = tips.groupby(["day", "smoker"])
print("============as index false")
print(tips.groupby(["day", "smoker"], as_index=False).sum())
print("============as index true")
print(tips.groupby(["day", "smoker"]).sum())
print("============")
#mantem o agrupamentgo por dia e fumante, mas focando na coluna tip_pct
grouped_pct = grouped["tip_pct"]
print(grouped_pct.head())
print("============")
#passando mais de uma funcao para 2 colunas agregadas
#ainda tem acesso ao agrupamento dia e fumante, pq o group by mantem ele encapsulado dentro da variavel
#ao passar um lupa, podemos passar o nome que vai na coluna e a funcao
f = grouped_pct.agg([("average", "mean"), ("stdev", "std")])
print(f)

print("===========")
#funcoes diferentes por colunas
print(grouped.agg(
    {
        "tip_pct" : ["min", "max", "mean", "std"],
        "size" : "sum"
    }
))