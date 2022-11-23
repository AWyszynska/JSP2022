import itertools
a = [1,2,3]
def lista(x):
    return list(itertools.permutations(x))

print(lista(a))


