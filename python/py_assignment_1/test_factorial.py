"""
This module contains unit tests for the factorial functions defined in the factorial module.
"""
from unittest import TestCase, main
from py_assignment_2.factorial import factorial, factorial_by_recur

class TestFactorialMethods(TestCase):
    """
    Test cases for the factorial functions.
    
    This class contains unit tests for the factorial functions defined in the
    factorial module. It tests both the iterative and recursive implementations
    of the factorial calculation.
    """

    def test_factorial_positive(self):
        """
        Test the iterative factorial function with positive numbers.
        
        This test checks the factorial function with positive integer inputs,
        including:
        - A small positive integer: 5
        - A larger positive integer: 10
        """
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_zero(self):
        """
        Test the iterative factorial function with zero.
        
        This test checks the factorial function with the input 0.
        """
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        """
        Test the iterative factorial function with negative numbers.
        
        This test checks that the factorial function raises an exception
        for negative input.
        """
        with self.assertRaises(Exception):
            factorial(-5)

    def test_factorial_by_recur_positive(self):
        """
        Test the recursive factorial function with positive numbers.
        
        This test checks the factorial_by_recur function with positive integer inputs,
        including:
        - A small positive integer: 5
        - A larger positive integer: 10
        """
        self.assertEqual(factorial_by_recur(5), 120)
        self.assertEqual(factorial_by_recur(10), 3628800)

    def test_factorial_by_recur_zero(self):
        """
        Test the recursive factorial function with zero.
        
        This test checks the factorial_by_recur function with the input 0.
        """
        self.assertEqual(factorial_by_recur(0), 1)

    def test_factorial_by_recur_negative(self):
        """
        Test the recursive factorial function with negative numbers.
        
        This test checks that the factorial_by_recur function raises an exception
        for negative input.
        """
        with self.assertRaises(Exception):
            factorial_by_recur(-5)

if __name__ == "__main__":
    main()
