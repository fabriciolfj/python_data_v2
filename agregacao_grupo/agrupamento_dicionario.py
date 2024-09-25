import pandas as pd
import numpy as np

people = pd.DataFrame(np.random.standard_normal((5, 5)),
                      columns=["a", "b", "c", "d", "e"],
                      index=["Joe", "Steve", "Wanda", "Jill", "Trey"])

people.iloc[2:3, [1, 2]] = np.nan

print(people)

mapping = {
    "a" : "red",
    "b" : "red",
    "c" : "blue",
    "d" : "blue",
    "e" : "red",
    "f" : "orange"
}

by_column = people.groupby(mapping, axis="columns")
print("================")
print(by_column.sum())
map_series = pd.Series(mapping)
by_column = people.groupby(map_series, axis="columns")
print("================")
print(by_column.count())

#usando uma funcao
print("================")
print(people.groupby(len).sum())