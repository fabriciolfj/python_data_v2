import pandas as pd
import matplotlib.pyplot as plt

tips = pd.read_csv("../files/tips.csv")

print(tips.head())

print("==========crosstab")
party_counts = pd.crosstab(tips["day"], tips["size"])
print(party_counts)

print("==========crosstab removendo grupo de 1 e 6 pessoas")
party_counts = party_counts.loc[:, 2:5]
print(party_counts)

print("==========normalizando proporcao de 1, onde somo cada valor da linha pela soma da linha")
party_pcts = party_counts.div(party_counts.sum(axis="columns"), axis="index")
print(party_pcts)

party_pcts.plot.bar(stacked=True)

plt.show()