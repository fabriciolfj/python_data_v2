import numpy as np

nsteps = 1000


rng = np.random.default_rng(seed=12345)
draws = rng.integers(0, 2, size=nsteps)


steps = np.where(draws == 0, 1,  -1)

walk = steps.cumsum()

print(walk.min())

print(walk.max())

#retorna  o primeiro index com value true, ou seja, a distancia de 10 passos nesse contexto
result = (np.abs(walk) >= 10).argmax()
print(result)