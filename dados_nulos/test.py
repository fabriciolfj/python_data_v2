import pandas as pd
import numpy as np

dados = pd.Series([1, 2, 3, None, 5])

result = dados.dropna()
print(result)


data = pd.DataFrame(
    [
        [1., 6.5, np.nan],
        [1., np.nan, np.nan],
        [np.nan, np.nan, np.nan],
        [np.nan, 6.5, np.nan],
    ]
)

print(data)

print("===================")

#por default tira as linhas que tiverem ao menos um Nan (null)
result = data.dropna()
print(result)

print("===================")
#vai remover as linhas que todos os valores sao nan
result = data.dropna(how="all")
print(result)

print("===================")
#vai remover as colunas que todos os valor
result = data.dropna(how="all", axis="columns")
print(result)

print("===================")
#passar um numero maximo (por linha ou coluna) de nan que deve constar, que queira manter
result = data.dropna(thresh=1)
print(result)

#substituindo valores ausentes por um valor default
print("===================")
result = data.fillna(0)
print(result)


#substituindo valores ausentes por um valor default, diferente por coluna
print("===================")
result = data.fillna({1: 5, 2 : 0})
print(result)