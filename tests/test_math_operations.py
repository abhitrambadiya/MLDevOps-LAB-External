"""
Unit tests for core multiplication logic (math_operations.py).
Tests various numeric inputs, mathematical properties, and edge cases.
"""

import sys
import os
import pytest

# Ensure src is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from math_operations import multiply


def test_positive_integers():
    """Test multiplication of two positive integers."""
    assert multiply(5, 10) == 50
    assert multiply(12, 12) == 144
    assert multiply(7, 8) == 56


def test_negative_numbers():
    """Test multiplication with negative integers."""
    assert multiply(-4, 5) == -20
    assert multiply(6, -3) == -18
    assert multiply(-8, -4) == 32


def test_multiplication_with_zero():
    """Test multiplication with zero (absorbing element)."""
    assert multiply(0, 10) == 0
    assert multiply(25, 0) == 0
    assert multiply(0, 0) == 0
    assert multiply(-15, 0) == 0


def test_multiplication_with_one():
    """Test multiplication with one (identity element)."""
    assert multiply(1, 42) == 42
    assert multiply(99, 1) == 99
    assert multiply(-7, 1) == -7


def test_floating_point_numbers():
    """Test multiplication of floating point numbers."""
    assert multiply(2.5, 4.0) == 10.0
    assert multiply(0.5, 0.5) == 0.25
    assert pytest.approx(multiply(0.1, 0.2), 0.0001) == 0.02
    assert multiply(-1.5, 2.0) == -3.0


def test_commutative_property():
    """Verify that a * b == b * a for various sets of numbers."""
    test_pairs = [(4, 9), (-3, 15), (2.5, 7.8), (0, 100)]
    for a, b in test_pairs:
        assert multiply(a, b) == multiply(b, a)


def test_string_numeric_conversion():
    """Verify string representations of numbers are safely converted."""
    assert multiply("10", "5") == 50.0
    assert multiply("2.5", 4) == 10.0


def test_invalid_type_raises_type_error():
    """Ensure invalid inputs like words, lists, None raise TypeError."""
    with pytest.raises(TypeError):
        multiply("abc", 5)

    with pytest.raises(TypeError):
        multiply(5, "xyz")

    with pytest.raises(TypeError):
        multiply(None, 10)

    with pytest.raises(TypeError):
        multiply([1, 2], 3)


def test_boolean_rejection():
    """Ensure booleans are rejected even though bool is a subclass of int in Python."""
    with pytest.raises(TypeError):
        multiply(True, 10)

    with pytest.raises(TypeError):
        multiply(5, False)
