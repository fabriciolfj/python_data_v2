import numpy as np

# Criando um numpy array
array = np.array([1, 2, 3, 4, 5])

print("Array created: ", array)

# Adicionar um número em todos os elementos do array
array = array + 5
print("Array after addition: ", array)

# Multiplicar todos os elementos do array por um número
array = array * 2
print("Array after multiplication: ", array)

# Calcular a soma de todos os elementos do array
sum = np.sum(array)
print("Sum of all elements: ", sum)
