from functools import reduce


def product(x, y):
    return x * y

print(reduce(product, [1, 2, 3, 4, 5]))
