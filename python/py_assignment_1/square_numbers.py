"""
This module provides a function to calculate the square of each number in a list.
"""

def square_num(number_list):
    """
    Calculate the square of each number in a list.

    Parameters:
    number_list (list of int): A list of integers.

    Returns:
    list of int: A list containing the square of each integer from the input list.
    """
    for index, value in enumerate(number_list):
        number_list[index] = value * value
    return number_list

if __name__ == '__main__':
    input_numbers = list(map(int, input().split()))
    print(square_num(input_numbers))
