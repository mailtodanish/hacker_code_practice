# MM DD YYYY
import calendar
ip = list(map(int, input().split()))
days = list(calendar.day_name)
day = days[calendar.weekday(ip[2],ip[0],ip[1])]
print(day.upper())