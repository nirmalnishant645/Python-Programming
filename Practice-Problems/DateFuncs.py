import datetime

print("Current date and time is:",datetime.datetime.now())
print("Today's date is:",datetime.date.today())
print("Date after 1326244364 seconds from 01-01-1970(timestamp)",datetime.date.fromtimestamp(1326244364))
print("Difference between 24-10-2018 and 21-03-2018 is:",(datetime.date(year = 2018, month = 10, day = 24))-(datetime.date(year = 2018, month = 3, day = 21)))
print("Time difference between 2 weeks-5 days-1 hour-33 seconds and 4 days-11 hours-4 minutes is: ",datetime.timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)-datetime.timedelta(days = 4, hours = 11, minutes = 4, seconds = 54))
