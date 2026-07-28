# Decorators let you add extra behaviour to a function, without changing the function's code.
# A decorator is a function that takes another function as input and return a new function.

def greet(func):
    def wrapper(*args):
        print("gud morning sir")
        func(*args)
        print("Thanks!")
    return wrapper

@greet
def fun(a,b):
    print(a+b)


fun(2,3)