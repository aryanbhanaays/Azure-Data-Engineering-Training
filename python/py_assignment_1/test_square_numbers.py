"""
This module contains unit tests for the square_num function defined in the square_numbers module.
"""
from square_numbers import square_num

def test_square_positive_numbers():
    """
    Test that the square_num function returns the correct squares of positive numbers.
    """
    assert square_num([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]

def test_square_negative_numbers():
    """
    Test that the square_num function returns the correct squares of negative numbers.
    """
    assert square_num([-1, -2, -3]) == [1, 4, 9]

def test_square_mixed_numbers():
    """
    Test the mix of positive, negative, and zero.
    """
    assert square_num([0, -1, 2, -3, 4]) == [0, 1, 4, 9, 16]
