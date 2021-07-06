'''
Peter wants to generate some prime numbers for his cryptosystem.
Help him! Your task is to generate all prime numbers between two given numbers!

Input
The input begins with the number t of test cases in a single line (t<=10).
In each of the next t lines there are two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

Output
For every test case print all prime numbers p such that m <= p <= n, one number per line, test cases separated by an empty line.

Example:
Input:
2
1 10
3 5
Output:
2
3
5
7

3
5

Warning: large Input/Output data, be careful with certain languages (though most should be OK if the algorithm is well designed)
'''

from math import sqrt

t = int(input())
while t:
    a, b = map(int, input().split())
    for i in range(a, b+1):
        flag = True
        if i > 1:
            for j in range(2, int(sqrt(i)) + 1):
                if not i % j:
                    flag = False
                    break
            if flag:
                print(i)
    t -= 1