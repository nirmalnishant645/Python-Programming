def isPalindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return isPalindrome(word[1:-1])

word = input("Enter a string: ")
if (isPalindrome(word) == True):
    print("Palindrome")
else:
    print("Not a Palindrome")
