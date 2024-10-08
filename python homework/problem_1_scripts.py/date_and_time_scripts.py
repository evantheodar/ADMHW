
###1 Calendar Module
import calendar

def find_day(month, day, year):
    day_index = calendar.weekday(year, month, day)
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    
    return days[day_index]

# Input format MM DD YYYY
date_input = input().split()

month = int(date_input[0])
day = int(date_input[1])
year = int(date_input[2])

# Output the correct day in capital letters
print(find_day(month, day, year))


###2 Time Delta
from datetime import datetime
import math


def time_difference(t1, t2):

    time_format = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, time_format)
    dt2 = datetime.strptime(t2, time_format)
    
    difference = abs((dt1 - dt2).total_seconds())
    
    return int(difference)

T = int(input())
for _ in range(T):
    t1 = input().strip()
    t2 = input().strip()
    print(time_difference(t1, t2))
