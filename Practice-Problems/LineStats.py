str = input("Enter a string: ")
upper, lower, digit, special = 0, 0, 0, 0
for i in range(len(str)):
    if str[i] >= 'A' and str[i] <= 'Z':
        upper += 1
    elif str[i] >= 'a' and str[i] <= 'z':
        lower += 1
    elif str[i] >= '0' and str[i] <= '9':
        digit += 1
    else:
        special += 1

print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
print("Number of alphabets:", upper+lower)
print("Number of digits:", digit)
