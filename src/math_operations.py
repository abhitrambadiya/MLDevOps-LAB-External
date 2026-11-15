"""
Math operations module for multiplication.
Provides core arithmetic functions with type validation and edge case handling.
"""

from typing import Union

Number = Union[int, float]


def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers and return the product.

    Args:
        a (int | float): The first number.
        b (int | float): The second number.

    Returns:
        int | float: The multiplication result of a and b.

    Raises:
        TypeError: If either input cannot be interpreted as a number (int or float).
    """
    # Reject booleans (in Python, bool is a subclass of int, e.g. True == 1)
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError(f"Invalid input: booleans are not allowed (a={a}, b={b})")

    if not isinstance(a, (int, float)):
        try:
            a = float(a)
        except (ValueError, TypeError):
            raise TypeError(f"Invalid input: 'a' must be a numeric value, got {type(a).__name__}: {a}")

    if not isinstance(b, (int, float)):
        try:
            b = float(b)
        except (ValueError, TypeError):
            raise TypeError(f"Invalid input: 'b' must be a numeric value, got {type(b).__name__}: {b}")

    result = a * b
    # If both inputs were integers, return integer, else float
    if isinstance(a, int) and isinstance(b, int):
        return int(result)
    return round(float(result), 10)
