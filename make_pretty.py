
def make_prettier(func):
    def inner():
        print("I was decorated")
        func()
    return inner


def normal():
    print("i am totally normal")

pretty = make_prettier(normal)
# pretty()

@make_prettier
def orinaray():
    print("I am ordinary")


orinaray()
