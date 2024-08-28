import numpy as np


arr = np.arange(10)

#savez salvar varios arrays, extencao npz
np.save("same_array", arr)

#load com arquivo de varios array, retorna um dicionario
arch = np.load("same_array.npy")
print(arch)