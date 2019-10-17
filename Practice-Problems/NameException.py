# Write a Program to generate an Exception when the name enter by user contains numeric or special symbol
import string

no = (set(string.digits) | set(string.punctuation))

a = input("Enter your name: ")

if (set(a)&no==set()):
    print("You Entered:",a)
else:
    try:
        raise ValueError('Numeric or Special Symbol cannot be in a name!')
    except ValueError:
        print('An exception flew by!')
        raise
