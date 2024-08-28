from random import random

import numpy as np

rng = np.random

arr = rng.standard_normal((4, 8))

print((arr > 0).sum())

arr = np.array([False, True, False])

print(arr.all())
print(arr.any())

#muda o resultado, se der true muda pra false e assim por diante
print(~arr.all())
print(~arr.any())