'''
Have the function EvenPairs(str) take the str parameter being passed and determine if a pair of adjacent even numbers exists anywhere in the string.
If a pair exists, return the string true, otherwise return false.
For example: if str is "f178svg3k19k46" then there are two even numbers at the end of the string, "46" so your program should return the string true.
Another example: if str is "7r5gg812" then the pair is "812" (8 and 12) so your program should return the string true.

Examples:
Input: "3gy41d216"
Output: true

Input: "f09r27i8e67"
Output: false
'''

# T0 be checked for efficieny

def EvenPairs(strParam):
  for i in range(len(strParam)):
    count = 0
    num = ''
    while i < len(strParam) and '0' <= strParam[i] <= '9':
      num += strParam[i]
      temp = int(num)
      if not temp % 2:
        num = ''
        count += 1
      i += 1
    if count >= 2:
      return True
  return False