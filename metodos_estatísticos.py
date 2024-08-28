import numpy as np

rng = np.random

arr = rng.standard_normal((5, 4))

print(arr)

print(np.sum(arr))
print(np.mean(arr))


arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.sum(axis=0))
print(arr.sum(axis=1))


print("===========")

arr = np.array([[1, 2],[3, 4], [5, 6]])
print(arr)
print(arr.sum(axis=0))
print(arr.sum(axis=1))
