'''
Calculate the difference between the current time and yesterday's time i.e. 2018-10-15 11:0:0:0
Calculate the Time Difference
Calculate the Days Difference
Calculate the Seconds Difference
'''
import datetime
yesterday = datetime.datetime(2018,10,15,11,0,0,0)
now = datetime.datetime.now()
print("Difference in Time: ",now-yesterday)
print("Difference in Days: ",(now-yesterday).days)
print("Difference in Seconds: ",(now-yesterday).total_seconds())
