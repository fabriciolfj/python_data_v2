import pandas as pd
import numpy as np

data = {
    "state" : ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
    "year" : [2010, 2011, 2012, 2013, 2014, 2015],
    "pop" : [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
}

frame = pd.DataFrame(data)

frame.head() #seleciona as 5 primeiras linhas
frame.tail() #seleciona as 5 ultimas
print(frame)

frame2 = pd.DataFrame(data, columns=["year", "state", "pop", "debit"]) #organizando ou ordenando as colunas, se colocar uma coluna sem dados, vai aparecer NaN


print(frame.year)
print("==============")

print(frame.loc[1]) #pegando a linha pelo index

print("==============")
frame2["debit"] = np.arange(6.)

print(frame2)

print("==============")
frame2["eastern"] = frame2["state"] == "Ohio" #passar uma coluna que nao existe, a mesma será criada, e nesse caso nao conseguiremos tb usar o dataframe.column
print(frame2)

del frame2["eastern"]
print(frame2)

#quando temos dicionarios aninhados, as chaves dos meis internos, vira index
populations = { "Ohio" : { 2000 : 1.5, 2001: 1.7, 2002: 3.6},
                "Nevada" : { 2001 : 2.4, 2002: 2.9 }}

frame3 = pd.DataFrame(populations)
print(frame3)

#troca linhas pelas colunas, mas devem ter o mesmo tipo, se nao será descartados
print(frame3.T)

# se passar o index, eles substituirao as chaves internas do dic
frame3 = pd.DataFrame(populations, index=[2001, 2002, 2003])

print("==============")
frame3.index.name = "year"
frame3.columns.name = "state"
print(frame3)

print(frame3.columns)

print("Ohio" in frame3.columns)

print(frame3.drop("Ohio", axis=1))