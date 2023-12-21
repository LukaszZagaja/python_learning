from datetime import date
from datetime import datetime

date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)

result = date1 - date2
print(result)
print(type(result))
print(result.days)
print("\n\n")

datetime1 = datetime(2021, 11, 3, 22, 0)
datetime2 = datetime(2020, 11, 3, 12, 0)

mydiff = datetime1 - datetime2
print(mydiff)

myseconds = mydiff.seconds
print(myseconds)
mytotalseconds = mydiff.total_seconds()
print(mytotalseconds)