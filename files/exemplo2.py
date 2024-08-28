import pandas as pd

#usando espaco como delimitador
df = pd.read_csv("ex3.txt", sep="\s+")
print(df)

#pulando linas
df = pd.read_csv("ex4.csv", skiprows=[0, 2, 3])
print(df)

#lidando com dados faltantes
df = pd.read_csv("ex5.csv")
print(df)

#colocando strings que sao reconhecidas como NaN
df = pd.read_csv("ex5.csv", na_values=["NULL"])
print(df)

print(pd.isna(df))