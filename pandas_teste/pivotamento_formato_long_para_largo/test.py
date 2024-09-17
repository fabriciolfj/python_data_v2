import pandas as pd
#formato long para largo, largo quanto os itens viram colunas (sao paulo, arroz, feijao)
#largo para long, quando as variaveis se tornam colunas (categoria, estado e etc)

data = pd.read_csv("../../files/macrodata.csv")
data = data.loc[:, ["year", "quarter", "realgdp", "infl", "unemp"]]

print("=========normal")
print(data.head())
print("=========periods")
periods = pd.PeriodIndex.from_fields(year=data.pop("year"), quarter=data.pop("quarter"))
print(periods)
print("=========index")
data.index = periods.to_timestamp("D")
print(data.head())
print("=========reindex")
data = data.reindex(columns=["realgdp", "infl", "unemp"])
data.columns.name = "item"
data.index.name = "date"
print(data.head())
print("========= stack")
long_data = (data.stack()
.reset_index().rename(columns={0: "value"}))                #reset_index transforma uma Series com multiindex em um dataframe

print(long_data[:10])
print("=========")
pivoted = long_data.pivot(index="date", columns="item", values="value")         #transformando para largo
print(pivoted.head())