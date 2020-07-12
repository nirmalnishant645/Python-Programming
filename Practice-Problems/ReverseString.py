'''
This question requires you to reverse a string using recursion.
Make sure to think of the base case here.

Again, make sure you use recursion to accomplish this.
Do not slice (e.g. string[::-1]) or use iteration, there must be a recursive call for the function.
'''

def reverse(s):

    # Base Case
    if len(s) == 1:
        return s

    # Recursion
    return reverse(s[1:]) + s[0]
