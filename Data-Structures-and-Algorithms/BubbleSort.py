#Bubble Sort Algorithm

def bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        flag = True
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False
        if flag:
            break

arr = [42,52,36,51,46,86,53,12]
bubbleSort(arr)
print(arr)

#Best Case, already sorted arr[], Time Complexity O(n)
#Worst Case, arr[] sorted in opposite direction, Time Complexity O(n*n)
#Average Case, Time Complexity O(n*n)

#Space Complexity, O(1)
