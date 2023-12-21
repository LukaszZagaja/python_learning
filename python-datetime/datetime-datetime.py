from datetime import datetime

mydatetime = datetime(2021, 10, 3, 14, 20, 1) #year, month, day, hour, minute, second
print(mydatetime)
mydatetime = mydatetime.replace(year=1990)
print(mydatetime)