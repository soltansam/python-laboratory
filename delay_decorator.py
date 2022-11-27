def delay_decorator(func):
    def wrapper_function():
        print("Add sth before the function call...")
        func()
        print("Print sth just after the function call...")
    return wrapper_function


@delay_decorator
def greet():
    print("hello!")


greet()
