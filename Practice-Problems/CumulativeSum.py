'''
Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer

For example, if n=4 , return 4+3+2+1+0, which is 10.
'''

def cumulative_sum(n):

    return 0 if not n else n + cumulative_sum(n - 1)