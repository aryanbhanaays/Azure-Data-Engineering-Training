# Using Function
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n <= 1:
        return 1
    fac=1
    while(n>=1):
        fac*=n
        n-=1
    return fac

# Using Recursion  
def factorial_by_recur(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n <= 1:
        return 1
    return n * factorial_by_recur(n - 1)

print(factorial_by_recur(-5))