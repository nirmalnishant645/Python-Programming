'''
Given a sorted array with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.

Note: If the number x is not found in the array just print '-1'.

Input:
The first line consists of an integer T i.e number of test cases. The first line of each test case contains two integers n and x. The second line contains n spaced integers.

Output:
Print index of the first and last occurrences of the number x with a space in between.

Constraints:
1<=T<=100
1<=n,a[i]<=1000

Example:
Input:
2
9 5
1 3 5 5 5 5 67 123 125
9 7
1 3 5 5 5 5 7 123 125

Output:
2 5
6 6
'''
def occur(arr, n, x, flag):
    lower, upper = 0, n-1

    while (lower<=upper):
        mid = (lower+upper)//2

        if ((arr[mid]==x and flag == 1) or arr[mid]<x):
            lower = mid+1
        else:
            upper = mid-1

    return upper if flag == 1 else lower

t = int(input())
while(t>0):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    upper = occur(arr, n, x, 1)
    if (arr[upper]!=x):
        print(-1)
    else:
        lower = occur(arr, n, x, 0)
        print(lower, upper)
    t-=1
