import pandas as pd


df = pd.read_csv('ex1.csv')

print(df)


df = pd.read_csv("ex2.csv", names=["a", "b", "c", "d",  "message"])
print(df)


#colocando como index os valores da coluna message
df = pd.read_csv("ex2.csv", names=["a", "b", "c", "d",  "message"], index_col="message")
print(df)


#index hierárquico
parse = pd.read_csv("csv_mindex.csv", index_col=["key1", "key2"])
print(parse)