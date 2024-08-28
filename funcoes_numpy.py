import numpy as np

rng = np.random.default_rng()

data = rng.standard_normal((2, 3))

#print(data)

#print("===========")

x = rng.standard_normal(8)

y = rng.standard_normal(8)

#print(x)
#print("===========")
#print(y)

value = np.maximum(x, y)
#print(value)

#print(y)
print("===========")
out = np.zeros_like(x)
#print(out)

#ele pega valores e y, soma 1 a cada elemento, e coloca no array out
np.add(y, 1, out=out)
#print(out)


a = [1, 2]
b = [3, 4]
a = [1, 2]
b = [3, 4]

result = np.meshgrid(a, b)
print(result)
result = np.meshgrid(a, b)
#print(result)


arr = rng.standard_normal((4,4 ))

#condicao where
result = np.where(arr > 0, 2, -2)
print(result)