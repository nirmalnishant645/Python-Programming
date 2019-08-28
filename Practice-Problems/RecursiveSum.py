def RSum(n):
    if n <= 1:
        return n
    return n + RSum(n - 1)

n = int(input("Enter the number upto which sum is required: "))
if (n < 0):
    print("Please enter a natural number!")
else:
    print(RSum(n))
