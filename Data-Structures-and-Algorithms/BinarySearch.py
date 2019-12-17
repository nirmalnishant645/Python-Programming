#Binary Search Algorithm in List

def BinarySearch(arr, target):
    lower, upper = 0, len(arr)-1
    
    while(lower<=upper):
        mid = (lower+upper)//2
        
        if (arr[mid] == target):
            return True
        if (arr[mid]<target):
            lower = mid+1
        else:
            upper = mid-1
    return False
    
#Best Case, target at arr[mid], Time Complexity O(1)
#Worst Case, target not in arr[], Time Complexity log(n)
#Average Case, target anywhere in the loop but in arr[mid], Time Complexity log(n)

#Space Complexity, O(1)
