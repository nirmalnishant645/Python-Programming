'''
Define a function to convert minutes to hours and use it to print the hour value
Define another function to convert seconds to hours and use it to print the hour value
'''

def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours

def seconds_to_hours(seconds):
    hours = seconds / 3600
    return hours

print (minutes_to_hours(70),"Hr")
print (seconds_to_hours(7200),"Hr")
