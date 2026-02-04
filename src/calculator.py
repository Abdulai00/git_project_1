"""Basic calculator operations."""
<<<<<<< HEAD
import math
=======
>>>>>>> f1deb16 (Initial commit: Calculator project structure)

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
<<<<<<< HEAD

def square_root(a):
    """Calculate square root of a."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)
=======
>>>>>>> f1deb16 (Initial commit: Calculator project structure)
