#Kadane’s algorithm is a Dynamic Programming approach to solve “the largest contiguous elements in an array” with runtime of O(n).

def kadane(arr):
    if len(arr)==0:
        return 0
    summ = maxSum = arr[0]
    for i in range(1, len(arr)):
        summ = arr[i] if summ<0 else summ+arr[i]
        maxSum = summ if summ>maxSum else maxSum
    return maxSum
