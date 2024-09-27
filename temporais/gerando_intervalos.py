import pandas as pd


index = pd.date_range("2012-04-01", "2012-04-08")
print(index)

print("=============")

index = pd.date_range(start="2012-04-01",periods=5, freq="B")
print(index)

print("=============")

index = pd.date_range(start="2012-04-01",periods=5, freq="4B")
print(index)

print("=============")

index = pd.date_range(start="2012-01-01", periods=10, freq="B")
print(index)

print("=============")

index = pd.date_range(start="2012-04-01",periods=5, freq="1h30min")
print(index)


#obter dadtas da terceira sexta de cada mes
index = pd.date_range(start="2012-04-01",periods=5, freq="WOM-3FRI")
print(index)