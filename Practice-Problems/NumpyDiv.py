a = input("Enter the numbers: ").split()
a = list(map(int, a))
print(a)
b = int(input("Enter the divisor: "))

#Method 1
for i in a:
    print(i,"-",i//b)

#Method 2
import numpy as np
print("Largest integer smaller or equal to the division of the inputs:")
print(np.floor_divide(a, b))
