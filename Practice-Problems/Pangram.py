import string

alphabet = set(string.ascii_lowercase)
phrase = input("Enter a phrase: ")

if(set(phrase.lower())>=alphabet):
    print("'%s' is a Pangram." % phrase)
else:
    print("'%s-' is not a Pangram." % phrase)
