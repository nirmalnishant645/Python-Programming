'''
Have the function FormattedNumber(strArr) take the strArr parameter being passed,
which will only contain a single element,
and return the string true if it is a valid number that contains only digits with properly placed decimals and commas,
otherwise return the string false.
For example: if strArr is ["1,093,222.04"] then your program should return the string true,
but if the input were ["1,093,22.04"] then your program should return the string false.
The input may contain characters other than digits.

Examples
Input: ["0.232567"]
Output: true

Input: ["2,567.00.2"]
Output: false
'''

# Efficiency to be checked

def addCommas(x):
    if x < 1000:
        return str(x)
    else:
        return addCommas(x // 1000) + ',' + '%03d' % (x % 1000)

def FormattedNumber(strArr):
    s = strArr.split('.')
    if len(s) > 2:
        return False
    temp = s[0]
    temp = temp.replace(',', '')
    temp = int(temp)
    temp = addCommas(temp)
    if temp != s[0]:
        return False
    for num in s:
        if num < '0' or num > '9':
            return False
    return True