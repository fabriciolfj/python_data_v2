import pandas_teste as pd

df = pd.read_csv('ex5.csv', na_values='NULL')
print(df)

df.to_csv('out.csv', na_rep='NULL', columns=['a', 'b', 'c'], sep='|')
