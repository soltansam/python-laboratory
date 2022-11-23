def my_function(message):

    def my_inner():
        print(message)
    return my_inner


chap = my_function('hello')

chap()
