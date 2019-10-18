import pandas as pd
import numpy as np

exam_data  = {'name': ['Nishant', 'Nirmal', 'Gaurav', 'Swapnil', 'Himanshu', 'Swastika', 'Vaishali', 'Laxmi', 'Anant', 'Mehak'],
        'score': [25, 19, 16, 17, 9, 20, 14, 15, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print(df)
