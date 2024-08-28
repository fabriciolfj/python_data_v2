def apply(some_list, func):
    return [func(v) for v in some_list]


ints = [4, 0, 1, 5, 6]
result = apply(ints, lambda x: x * 2)

print(result)