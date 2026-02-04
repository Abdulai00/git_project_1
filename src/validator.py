<<<<<<< HEAD
"""
This module checks that the user inputs make sense and that the outputs are relevant.
"""
=======
"""Input validation for calculator."""

>>>>>>> f1deb16 (Initial commit: Calculator project structure)
def validate_number(value):
    """Validate that value can be converted to a number."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def validate_operation(op):
    """Validate that operation is supported."""
    valid_ops = ['+', '-', '*', '/']
    return op in valid_ops
<<<<<<< HEAD

def validate_non_negative(n):
    """Validate that a number is non-negative."""
    try:
        num = float(n)
        return num >= 0
    except (ValueError, TypeError):
        return False
=======
>>>>>>> f1deb16 (Initial commit: Calculator project structure)
