
#!/usr/bin/python3
"""Create a functions for division."""


def safe_print_division(a, b):
    """Create a function for division."""
    result = None

    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {:}".format(result))
    return result
