arr = input("Enter numbers into the list: ").split()
arr = list(map(int, arr))
arr.sort()
print(arr)
n = int(input("Enter the number to search in the list: "))

l = 0
u = len(arr)-1

while (l<=u):
    mid = (l+u)//2

    if (arr[mid] == n):
        print(("Position of %d is %d") % (n, mid))
        break
    else:
        if (arr[mid]<n):
            l = mid+1
        else:
            u = mid-1
else:
    print("Not found!")
