import itertools


def first_letter(x):
    return x[0]

names = ["Alan", "Adam", "Wes", "Will", "Albert", "Steven", "fabricio", "Atest"]

for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names))