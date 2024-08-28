import numpy as np

result = np.zeros(10)
print(result)

result = np.zeros((3, 6))
print(result)

data1 = [6, 1.0, 3, 5]
result = np.array(data1)
print(result)

result = np.arange(10)
print(result)


result = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.int64)
print(result.dtype)


#efetuando cast do array
float_arr = result.astype(np.float64)
print(float_arr.dtype)

#operacoes no array, de mesmo tamanho, nao precisa de for
arr_1 = np.array([3, 5, 8, 2])
arr_2 = np.array([4, 6, 2, 9])

result = arr_1 + arr_2
print(result)

result = arr_1 ** 2
print(result)

result = arr_1 > arr_2
print(result)

result = arr_1 == arr_2
print(result)


## fatias
result = arr_1[1:3]
print("primeira fatia")
print(result)

#se mudo a fatia, muda o array original

result[:] = 5
print(arr_1)
print("=================")

#milti dimensional
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)
print("=================")
#nao funciona nas listas padroes do pythoon
print(arr_2d[1, 1])

print("================= bi"
      "dimensional")
result = arr_2d[:2, 2]
print(result)

print("=================")
result = arr_2d[:, :1]
print(result)

#indexacao booleana
names = np.array(["Bob", "Joe", "Bob", "Will"])
data = np.array([[1, -22], [4, -55], [7, 8], [9, 8]])

print(names == "Bob")

result = data[names == "Bob"]
print(result)

#diferente de bobo
result = data[~(names == "Bob")]
print(result)

mask = (names == "Bob") | (names == "Joe")
print(data[mask])

print("=================")
#substituindo tudo que for menor que 0 por 0
data[data < 0] = 0
print(data)