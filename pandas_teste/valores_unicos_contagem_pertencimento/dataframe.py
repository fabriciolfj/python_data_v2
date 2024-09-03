import pandas as pd

data = pd.DataFrame(
    {"Qu1": [1, 3, 4, 3, 4],
     "Qu2": [2, 3, 1, 2, 3],
     "Qu3": [1, 5, 2, 4, 4]})

#calculando em uma coluna
print(data["Qu1"].value_counts().sort_index())


#calculando todas as colunas
print(data.apply(pd.value_counts).fillna(0).sort_index())

data = pd.DataFrame({"a": [1, 1, 3, 4], "b" : [1, 1, 3, 4]})

#calculando por lina
print(data.value_counts().sort_index())