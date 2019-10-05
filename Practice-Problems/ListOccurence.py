arr = input("Enter numbers into the list: ").split()
arr = list(map(int, arr))
n = int(input("Enter the number to find in th list: "))

print(("%d occurs %d time(s)") % (n, arr.count(n)))
