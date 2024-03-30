def decorator(foo:str):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            print("Foo", foo)
            return func(*args, **kwargs)
        return wrapper
    return inner_decorator

@decorator(foo="bar")
def my_function():
    print("Hello")

my_function()