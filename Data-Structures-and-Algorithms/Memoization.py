'''
Memoization effectively refers to remembering ("memoization" -> "memorandum" -> to be remembered) results
of method calls based on the method inputs and then returning the remembered result
rather than computing the result again.
It can be thought of as a cache for method results.
'''

import timeit

# Example for implementing a normal factorial function

def fact_normal(n):

    if not n:

        return 1

    else:

        return n * fact_normal(n - 1)

# Example for computing factorials using Memoization

lookup_table = {}

def fact(n):


    if not n:

        return 1
    
    if not n in lookup_table:

        lookup_table[n] = n * fact(n - 1)

    return lookup_table[n]

# Encapsulate the memoization process into a class

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def factorial(k):
    
    if k < 2: 
        return 1
    
    return k * factorial(k - 1)

factorial = Memoize(factorial)

print(timeit.timeit("fact_normal(100)", setup="from __main__ import fact_normal"))
print(timeit.timeit("fact(100)", setup="from __main__ import fact"))
print(timeit.timeit("factorial(100)", setup="from __main__ import factorial"))

# Time taken to execute fact_normal(100) = 17.656458724000004   [Normal]
# Time taken to execute fact(100) = 0.1724773260002621          [Memoisation]
# Time taken to execute factorial(100) = 0.36176484800034814    [Memoisation]