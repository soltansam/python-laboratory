


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print('this can not be divided')
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    return a/b


divide(40, 0)
