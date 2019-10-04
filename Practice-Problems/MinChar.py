s = input("Enter numerous strings: ").split()

print("Minimum number of characters:",min(s, key=len))
