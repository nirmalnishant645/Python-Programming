# Program will ask the user to enter a number until they guess a stored number correctly using user-defined exceptions.

# define Python user-defined exceptions
class Error(Exception):
   pass
class ValueTooSmallError(Error):
   pass
class ValueTooLargeError(Error):
   pass
   
number = 50
while True:
   try:
       num = int(input("Enter a number: "))
       if num < number:
           raise ValueTooSmallError
       elif num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("The number is definitely greater than",num)
       print()
   except ValueTooLargeError:
       print("The number is definitely smaller than",num)
       print()
print("You guessed it right!")
