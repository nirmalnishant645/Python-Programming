'''
Given an array of sorted integers. The task is to find the closest value to the given number in array. Array may contain duplicate values.

Note: If the difference is same for two values print the value which is greater than the given number.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains two integers N & K and the second line contains N space separated array elements.

Output:
For each test case, print the closest number in new line.

Constraints:
1<=T<=100
1<=N<=105
1<=K<=105
1<=A[i]<=105

Example:
Input:
2
4 4
1 3 6 7
7 4
1 2 3 5 6 8 9

Output:
3
5
'''
def BinarySearch(arr, n, k):
    lower, upper = 1, n-2

    while (lower<=upper):
        mid = (lower+upper)//2
        if (arr[mid]==k):
                return arr[mid]
        if (arr[mid]<k):
            lower=mid+1
        else:
            upper=mid-1
    return arr[upper] if (k-arr[upper]<arr[lower]-k) else arr[lower]

t = int(input())
while(t>0):
    n, k = [int(x) for x in input().split()]
    arr = list(map(int, input().split()))
    print(BinarySearch(arr, n, k))
    t-=1
