v = input("Enter a String: ")
vowels = "AaEeIiOoUu"
count=0
vow = [letter for letter in v if letter in vowels]
print(len(vow))
