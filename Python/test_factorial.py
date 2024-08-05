from unittest import TestCase, main
from factorial import factorial, factorial_by_recur

class TestFactorial(TestCase):
    
    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial_by_recur(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial_by_recur(0), 1)

    def test_factorial_negative(self):
            self.assertEqual(factorial(-5), "Factorial is not defined for negative numbers")
            self.assertEqual(factorial_by_recur(-5), "Factorial is not defined for negative numbers")


if __name__ == '__main__':
    main()
