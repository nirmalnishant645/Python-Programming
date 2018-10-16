'''
Store 5 time events in a list seperated by 1 second
'''
import datetime
import time
times=[]
for i in range(5):
    times.append(datetime.datetime.now())
    time.sleep(1)
print(times)
