"""
This module provides a function to calculate the square of each number in a list.
"""

def square(numbers):
    """
    Calculate the square of each number in a list.

    Parameters:
    numbers (list of int): A list of integers.

    Returns:
    list of int: A list containing the square of each integer from the input list.
    """
    return [i * i for i in numbers]

if __name__ == '__main__':
    input_numbers = list(map(int, input().split()))
    print(square(input_numbers))
