import pandas as pd
import numpy as np

df = pd.DataFrame(
    {"key": ["b", "b", "a", "c", "a", "b"],
     "data1" : range(6)}
)

print(df)

#preenche como 0(false) ou 1 (true), na coluna key quando apareceu a e depois b e c.
print("=============")
result = pd.get_dummies(df["key"], prefix="key")
print(result)

print("=============")
result = df[["data1"]].join(pd.get_dummies(df["key"], prefix="key").astype(int))
print(result)


mnames = ["movie_id", "title", "genres"]

movies = pd.read_table("../../datasets/movielens/movies.dat", sep="::", header=None, names=mnames, engine="python")
print(movies)

dummies = movies["genres"].str.get_dummies("|")
print("=============")
print(dummies.iloc[:10, :6])

movies_windic = movies.join(dummies.add_prefix("Genre_"))
print("=============")
print(movies_windic.iloc[0])

data = np.random.uniform(size=10)

bins = [0, 0.2, 0.4, 0.6, 0.8, 1]

print(pd.get_dummies(pd.cut(data, bins)).astype(int))