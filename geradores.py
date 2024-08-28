

#versao verbosa
def squares(n=10):
    print(f"generation squares from 1 to {n}")
    for i in range(n):
        yield i ** 2

#usando comprehensions
gen = (i ** 2 for i in range(10))

## geradores sao executados quando efetuamos uma iteracao
for x in gen:
    print(x)


gen = squares()

for x in gen:
    print(x)

