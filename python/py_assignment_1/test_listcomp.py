"""
This module contains unit tests for the square function defined in the square_list_comp module.
"""
from square_list_comp import square

def test_square_positive_numbers():
    """
    Test that the square function returns the correct squares of positive numbers.
    """
    assert square([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]

def test_square_negative_numbers():
    """
    Test that the square function returns the correct squares of negative numbers.
    """
    assert square([-1, -2, -3]) == [1, 4, 9]

def test_square_mixed_numbers():
    """
    Test the mix of positive, negative, and zero.
    """
    assert square([0, -1, 2, -3, 4]) == [0, 1, 4, 9, 16]
