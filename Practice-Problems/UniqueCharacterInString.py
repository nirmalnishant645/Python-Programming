'''
Given a string, determine if it has all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return False.
'''

# (One - Liner) Using Built-In Data Structure and Built-In Function

def uni_char(s):
    return len(set(s)) == len(s)
