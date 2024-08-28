import numpy as np
import pandas as pd

obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])

print(obj)

obj2 = obj.loc[['a', 'b', 'c']]
print(obj2)

#basea-se em inteiros
obj2 = obj.iloc[[0, 1, 2]]
print(obj2)

# com pandas o ultimo e incluido no resultado
obj2 = obj["b":"c"]
print(obj2)

print("===========")
obj = pd.DataFrame(np.arange(16).reshape(4, 4), index=['Ohio', 'Colorado', 'Utah', 'New York'],
                   columns=['one', 'two', 'three', 'four'])
#obj2 = obj["two"]
#print(obj2)

#pegar essas colunas
#obj2 = obj[["two", "one"]]
#print(obj2)

#obj2 = obj[:2]
#print(obj2)


#loc e iloc
obj2 = obj.loc["Colorado"]
print(obj2)

obj2 = obj.loc[["Utah", "New York"]]
print(obj2)

print("===========")
print(obj.loc[:, :][obj.three > 5])


print("===========")
print(obj.loc[obj.three > 5])


obj2 = obj.loc["Ohio": "New York"]
print(obj2)


obj.loc[obj.three <= 6] = 0
print(obj)

print(obj <= 6)

obj[obj.three <= 10] = 0
print(obj)