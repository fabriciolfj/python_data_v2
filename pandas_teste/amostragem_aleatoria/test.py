import pandas as pd

choices = pd.Series([5, 7, -1, 6, 4])
print(choices)
print("=============")

#subconjunto aleatorio com substituicao
result = choices.sample(n=10, replace=True)
print(result)

#subconjunto aleatorio sem substituicao
print("=============")
result = choices.sample(n=5, replace=False)
print(result)