import math
"""This file provides various calculation functions which can be used on integers and floats"""


def add(a, b):
    """Add two numbers."""
    result = a + b
    return result

def subtract(a, b):
    """Subtract b from a."""
    result = a - b
    return result

def multiply(a, b):
    """Multiply two numbers."""
    result = a * b
    return result

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")

    result = a / b
    return result

def square_root(a):
    """Calculate square root of a."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)

def power(a, b):
    """Raise a to the power of b."""
    result = a ** b
    return result

def modulo(a, b):
    """Return remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    result = a % b
    return result
    return a / b

def modulo(a, b):
    """Return remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
