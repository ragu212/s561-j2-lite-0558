def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def sub(a, b):
    return a - b


def div(a, b):
    """Return a divided by b; raise ZeroDivisionError when b is 0."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
