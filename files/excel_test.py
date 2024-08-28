import pandas as pd

xlsx = pd.ExcelFile('ex1.xlsx')

print(xlsx.sheet_names)

print(xlsx.parse(sheet_name='Sheet1', index_col=0))


frame = pd.read_excel('ex1.xlsx', sheet_name='Sheet1')


frame.to_excel('ex2.xlsx')