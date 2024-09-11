import pandas as pd
import numpy as np

fruits = ['apple', 'orange', 'apple', 'apple'] * 2

N = len(fruits)

rng = np.random.default_rng(seed=12345)

df = pd.DataFrame(
    {'fruit': fruits,
     'basket_id' : np.arange(N),
     'count': rng.integers(3, 15, size=N),
     'weight' : rng.uniform(0, 4, size=N)},
    columns=['basket_id', 'fruit', 'count', 'weight']
)

#convertendo para um tipo categorico
fruit_cat = df['fruit'].astype('category')
print(fruit_cat)

c = fruit_cat.array
print(type(c))
print(c.categories)
print(c.codes)
print(dict(enumerate(c.categories)))
print(c.value_counts())