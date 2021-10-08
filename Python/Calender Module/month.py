import calendar

yy=2021
mm=9

print("weekdays is ",calendar.weekday(yy,mm,23))
print(calendar.month(yy,mm))

print(calendar.calendar(1992))

obj = calendar.Calendar(firstweekday=0)

for day in obj.iterweekdays():
    print(day)

for day in obj.itermonthdates(2021,9):
    print(day)

# for day in obj.getfirstweekday():
#     print(day)

for day in obj.yeardayscalendar(1992):
    print(day)

cal = calendar.TextCalendar(firstweekday = 0)
print(cal.formatyear(2018,5, c=3, m=2))


