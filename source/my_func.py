# This function adds two numbers.
def add(x, y):
    return x + y


# This function subtracts y from x.
def subtract(x, y):
    return x - y


# This function mistakenly adds x and y instead of multiplying.
def multiply(x, y):
    return x * y


# This function divides x by y, handling the case where y is zero.
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError('zero division not possible!')
    return x / y
