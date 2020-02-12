'''
A fixed point in an array is an element whose value is equal to its index. 
Given a sorted array of distinct elements, return a fixed point, if one exists.
Otherwise, return False.
For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
'''

#Time Complexity - O(log n), Space Complexity - O(1)

def indexValue(arr):
    first, last = 0, len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if mid == arr[mid]:
            return mid
        if arr[mid] < mid:
            first = mid + 1
        else:
            last = mid - 1
    return False

arr = list(map(int, input().split()))
print(indexValue(arr))
