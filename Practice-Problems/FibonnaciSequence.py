'''
Implement a Fibonnaci Sequence in three different ways:

    - Recursively
    - Dynamically (Using Memoization to store results)
    - Iteratively

Function Output
Your function will accept a number n and return the nth number of the fibonacci sequence

Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,...
starts off with a base case checking to see if n = 0 or 1, then it returns 1.
Else it returns fib(n-1)+fib(n-2).
'''

# Iteratively
def fib_iter(n):

    res, next = 0, 1

    for i in range(n):

        res, next = next, res + next

    return res

# Recursively
def fib_rec(n):

    # Base Case
    if not n or n == 1:

        return n

    # Recursive Case
    else:

        return fib_rec(n - 1) + fib_rec(n - 2)

# Dynamically (Using Memoization to store results)
lookup_table = {}   # Instantiate Cache Information

def fib_dyn(n):

    if not n or n == 1: # Base Case

        return n

    if not n in lookup_table:   # Check Cache

        lookup_table[n] = fib_rec(n - 1) + fib_rec(n - 2)   # Set Cache
    
    return lookup_table[n]