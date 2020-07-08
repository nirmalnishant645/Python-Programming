'''
Given a string of opening and closing parentheses, check whether it's balanced.
We have 3 types of parentheses: 
    Round Brackets ()
    Square Brackets []
    Curly Brackets {}
Assume that the string doesn't contain any other character than these, no spaces, words or numbers.
As a reminder, balanced parentheses require every opening parentheses to be closed in the reversed order opened.
For example, '([])' is balanced but '([)]' is not.

You can assume the input string has no spaces.
'''

def balance_check(s):

    if len(s) % 2:
        return False
    
    matches = {')' : '(', ']' : '[', '}' : '{'}
    
    stack = []

    for paren in s:

        if paren in matches.values():
            stack.append(paren)

        else:

            if not len(stack) or stack.pop() != matches[paren]:
                return False
                
    return not stack