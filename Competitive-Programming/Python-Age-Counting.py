'''
In the Python file, write a program to perform a GET request on the route https://coderbyte.com/api/challenges/json/age-counting
which contains a data key and the value is a string which contains items in the format:
key=STRING, age=INTEGER. Your goal is to count how many items exist that have an age equal to or greater than 50, and print this final value.

Example Input
{"data":"key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"}

Example Output
2
'''

# Efficiency to be checked

import requests

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
data = (r.json()['data'])
total = 0
for item in data.split(","):
  if 'age' in item:
    if int(item[5:]) >= 50:
      total += 1
print(total)