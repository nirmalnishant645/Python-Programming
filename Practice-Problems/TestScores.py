'''
In this problem, you have to write a program that reads a file containing scores received by students in a number of subjects, and does some processing on it.

The input is being read in from a file called input.txt, in this format:

22, Data Structures, 45
23, English, 52
22, English, 51
26, Data Structures, 72
23, Data Structures, 61
26, English, 81

Each line consists of three fields "Student ID," "Subject," and "Marks."
"Student ID" and "Marks" are integers and "Subject" is a string that does not contain commas or newlines.
There can be any number of students and up to 6 subjects.
Your program should read this file, count the number of students whose total marks across all subjects is 100 or more, and write the count to a file called output.txt.

For example, if your program is run with the input given above, then at the end the file output.txt should contain just 2.
That's because 2 students (with ID 23 and 26) have aggregates scores of 100 or more.
'''
dict  = {}
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        line = line.strip()
        word = line.split(',')
        if word[0] in dict:
            dict[word[0]] += int(word[2])
        else:
            dict[word[0]] = int(word[2])
total = 0
for id, marks in dict.items():
    if marks >= 100:
        total += 1
f = open('output.txt', 'w')
f.write(str(total))
f.close()    