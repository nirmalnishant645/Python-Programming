'''
There are two main instances of recursion.
The first is when recursion is used as a technique in which a function makes one or more calls to itself.
The second is when a data structure uses smaller instances of the same type of data structure when it represents itself.
Both of these instances are use cases of recursion.

Recursion provides a powerful alternatice for performing repetitions of tasks in which loop is not ideal.
Most modern programming languages support recursion and recursion serves as a great tool for building our particular data structures.
'''

# FACTORIAL EXAMPLE

'''
Things to remember:
    - n! = n.(n-1)! (Recursive Pattern)
    - n = 0, n! = 1 (Base Case)
'''

def fact(n):

    if not n:

        return 1

    else:

        return n * fact(n - 1)