import calendar

print(calendar.weekheader(3))

print(calendar.firstweekday())

print(calendar.month(2021, 2))

print(calendar.monthcalendar(2021, 2))

print(calendar.calendar(2021))

day_of_the_week = calendar.weekday(2021, 2, 12)
print(day_of_the_week)

is_leap_2021 = calendar.isleap(2021)
is_leap_2020 = calendar.isleap(2020)
print(is_leap_2021)
print(is_leap_2020)

how_many_leap_days = calendar.leapdays(2000, 2021)
print(how_many_leap_days)