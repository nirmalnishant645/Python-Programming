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