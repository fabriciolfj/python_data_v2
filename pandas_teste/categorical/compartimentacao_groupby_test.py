import pandas as pd
import numpy as np

rng = np.random.default_rng(seed=12345)
draws = rng.standard_normal(1000)
##A função pandas.qcut é usada para dividir os dados em quantis. Quantis são valores que dividem os dados em intervalos de tamanhos iguais. Por exemplo, 4 quantis (também conhecidos como quartis) dividem os dados em 4 grupos com aproximadamente o mesmo número de observações em cada grupo.
bins = pd.qcut(draws, 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

print(bins.value_counts())

bins = pd.Series(bins, name='quartile')
print("=====================")
results = (pd.Series(draws).groupby(bins).agg(['count', 'min', 'max']).reset_index())
print(results)