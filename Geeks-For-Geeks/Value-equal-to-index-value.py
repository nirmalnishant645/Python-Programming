'''
Given an array of positive integers. Your task is to find that element whose value is equal to that of its index value.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N, size of array. The second line of each test case contains array elements.

Output:
Print the element whose value is equal to index value. Print "Not Found" when index value does not match with value.
Note: There can be more than one element in the array which have same value as their index. You need to print every such element's index separated by a single space. Follows 1-based indexing of the array.

Constraints:
1 ≤ T ≤ 30
1 ≤ N ≤ 50
1 ≤ A[i] ≤ 1000

Example:
Input:
2
5
15 2 45 12 7
1
1

Output:
2
1
'''
def LinearSearch(arr):
    result=[]
    for i in range(len(arr)):
        if (i+1 == arr[i]):
            result.append(i+1)
    return result if result else ["Not Found"]


T = int(input())
while(T>0):
    N = int(input())
    arr = list(map(int, input().split()))
    print(*LinearSearch(arr))
    T-=1
