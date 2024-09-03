import pandas as pd


obj = pd.Series(["c", "a", "d", "a", "a", "b",  "b", "c", "c"])

unique = obj.unique()

print(unique)

print(obj.value_counts())

##retorna um series boolean, onde o index indica a posicao eo o valor true ou false
mask = obj.isin(["b", "c"])
print(mask)

#retorna as posicoes que deu true no mask acima
print(obj[mask])

#retorna no array apenas os indexes distintos
print(pd.Index(unique).get_indexer(obj))