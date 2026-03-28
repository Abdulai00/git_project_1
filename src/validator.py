"""Input validation for calculator."""
#Experiment: testing reflog recovery

"""Input validation for calculator.
This mode checks if the given values are number, valid operation, 
are positive. 
"""
#This is layele expermential quote


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

"""Module for validating calculator inputs."""

def validate_non_negative(n):
    """Check if a number is greater than or equal to zero."""
    return n >= 0

def validate_positive(n):
    """Check if a number is strictly greater than zero."""
    # This matches your Checkpoint 3 helper function
    return n > 0

def validate_range(value, min_val=-1000, max_val=1000):
    """
    Ensure the value falls within the specified range.
    Returns True if within range, False otherwise.
    """
    try:
        # Convert to float to ensure we can compare numeric values
        num = float(value)
        return min_val <= num <= max_val
    except (ValueError, TypeError):
        # If the input isn't a number, it's technically not in the numeric range
        return False

        
# i think this commment is cool
def is_positive(n):
       """Check if a number is positive."""
       return n > 0
