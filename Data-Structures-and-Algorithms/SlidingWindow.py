# Implementing Sliding Window in Max Sum

def maxSum(arr, windowSize):
    arraySize = len(arr)
    if arraySize <= windowSize:
        print("Invalid Operation")
        return -1
    
    window_sum = sum(arr[i] for i in range(windowSize))
    max_sum = window_sum

    for i in range(arraySize - windowSize):
        window_sum = window_sum - arr[i] + arr[i + windowSize]
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [80, -50, 90, 100]
k = 2
answer = maxSum(arr, k) # 190
print(answer)