strings = ["as", "a", "bat", "car", "dove", "python"]


result = [a.upper() for a in strings if len(a) > 2]


print(result)

dic = {key: a for key, a in enumerate(strings)}
print(dic)

vales = [[1, 2, 3, 4], [5, 6, 7, 8]]

result = [x for v in vales for x in v]
print(result)