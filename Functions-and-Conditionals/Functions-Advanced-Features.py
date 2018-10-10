'''
Define a function to take two inputs as minutes and seconds and convert them into hour and print the final sum.
'''
def minutes_to_hours(minutes, seconds):
    hours = minutes / 60 + seconds / 3600
    return hours

print (minutes_to_hours(70, 300),"Hr")
