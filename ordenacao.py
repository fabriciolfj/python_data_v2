import numpy as np

#ordena a linha (olhando do eixo y - coluna)
arr = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
arr.sort(axis=1)
print(arr)

#ordena a coluna (olhando do eixo x - linha)
arr = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
arr.sort(axis=0)
print(arr)