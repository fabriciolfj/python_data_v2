import pandas as pd

data = {
    "cidade" : ["Serrana", "Serra Azul", "Cravinhos"],
    "year" : [2010, 2011, 2012,],
    "pop" : [1.5, 1.7, 3.6,]
}

frame = pd.DataFrame(data, columns=["cidade", "year", "pop"])

print(frame)

print("==================stack")
result = frame.stack()
print(result)
print("==================reindex")
result = result.reset_index().reindex()
print(result)

print("=========pivot index antigo")
test = result.pivot(index="level_0", columns="level_1", values=0).reset_index()
print(test.head())
print("=========pivot")
result = result.pivot(index="level_0", columns="level_1", values=0).reset_index(drop=True) #index antigo e descartado
print(result.head())