import calender
# Enter your code here. Read input from STDIN. Print output to STDOUT
mm, dd ,yy = map(int,input().split())

cal = calender.Calender(firstweekday=0)

print(cal.weekday())

