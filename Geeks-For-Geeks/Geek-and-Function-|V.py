'''
Given two integers numbers N and K, the Geek wants you to find f(f(..........f(N))) K times, where f(x) = x XOR (x%10).
Note: XOR represents bitwise xor operation

Input:
1. The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
2. The first line of each test case contains two integers N and K.

Output: For each test case, print the answer

Constraints:
1. 1 <= T <= 10
2. 1 <= N <= 105
3. 1 <= K <= 109

Example:

Input:
2
17 1
66 3

Output:
22
74
'''

t = int(input())

while t:
    n, k = input().split(' ')
    n, k = int(n), int(k)
    
    res = n
    
    for i in range(k):
        if not res % 10:
            break
        res ^= res % 10
        
    print(res)
    
    t -= 1