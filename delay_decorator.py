def delay_decorator(func):
    def wrapper_function():
        func()
    return wrapper_function


@delay_decorator
def greet():
    print("hello!")
