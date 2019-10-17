# Write a Code that accepts String in a format like "My name is someone"
# Then it has to be formatted into "MyNameIsSomeone" and then back to original.
import re
a = input().split()
a = [i.capitalize() for i in a]
b = ''.join(a)
print("Converted String:",b)
c = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', b)
c = re.sub('([a-z])([A-Z])', r'\1 \2', c).lower()
print("Original String:",c.capitalize())
