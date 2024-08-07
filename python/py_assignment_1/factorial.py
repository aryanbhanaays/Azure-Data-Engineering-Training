"""
This module provides two functions to calculate the factorial of a number:
1. factorial - using an iterative approach
2. factorial_by_recur - using a recursive approach
"""

def factorial(n):
    """
    Calculate the factorial of a number using an iterative approach.
    Parameters:
    n (int): The number for which to calculate the factorial
    Returns:
    int: The factorial of the number.
    Raises:
    NegativeNumberError: If the number is negative.
    """
    if n < 0:
        raise Exception("Factorial is not defined for negative numbers")
    fac = 1
    while n >= 1:
        fac *= n
        n -= 1
    return fac

def factorial_by_recur(n):
    """
    Calculate the factorial of a number using a recursive approach.
    Parameters:
    n (int): The number for which to calculate the factorial.
    Returns:
    int: The factorial of the number.
    Raises:
    NegativeNumberError: If the number is negative.
    """
    if n < 0:
        raise Exception("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial_by_recur(n - 1)

if __name__ == "__main__":
    try:
        print(factorial(-5))          
        print(factorial_by_recur(-5))
    except Exception as e:
        print(e)
