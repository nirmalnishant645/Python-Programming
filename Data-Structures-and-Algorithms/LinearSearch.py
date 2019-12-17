#Linear Search Algorithm in List

def LinearSearch(arr, target):
    for num in arr:
        if num == target:
            return True
    return False

#Best Case, target at arr[0], loop runs once, Time Complexity O(1)
#Worst Case, target not in the list, loop runs n times, Time Complexity O(n)
#Average Case, target at arr[1]-arr[n], loop runs at least twice or at most n times, Time Complexity remains O(n) (Constant not considered, n/2 changes to n)

#Since we are not using any extra data structure therefore the space complexity will be O(1)
