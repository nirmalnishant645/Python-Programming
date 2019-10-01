v = input("Enter a String: ")
vowels = "AaEeIiOoUu"
count=0
vow = [each for each in v if each in vowels]
print(len(vow))
