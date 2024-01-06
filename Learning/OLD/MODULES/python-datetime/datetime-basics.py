import datetime

mytime = datetime.time(16, 32, 5, 18) 
#print(mytime.minute())
#print(mytime.hour())
print(mytime) #Don't know why it isn't printed 
#print(mytime.microsecond())
print("\n")
print(type(mytime))
print("\n\n")

date1 = datetime.date(2020, 6, 23)
print(date1)
print(date1.month)
print("\n")

today = datetime.date.today()
print(today)
print(today.day)
print(today.year)
print("\n")
print(today.ctime())
print("\n")