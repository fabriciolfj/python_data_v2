import pandas as pd

df = pd.DataFrame(
    {
        "key": ["foo", "bar", "baz"],
        "A" : [1, 2, 3],
        "B" : [4, 5, 6],
        "C" : [7, 8, 9],
    }
)

#torna mais longo, mescla ou agropa os valores, no caso selecione a coluna key para ser agrupada
melted = pd.melt(df, id_vars=["key"])
print(melted)

#voltando como estava usando o pivot
reshaped = melted.pivot(index="key", columns="variable", values="value")
print("================")
print(reshaped.reset_index()) #reset_index para voltar o key a coluna e adicionar o index, obs: o pivot cria o index no que especificar