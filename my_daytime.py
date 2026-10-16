import datetime

now = datetime.datetime.now()

print(now.year) #kuvab praeguse aasta
print(now.month) #kuvab praeguse kuu numbri
print(now.day) #kuvab kuupäeva numbri
print(now.hour) #kuvab tunni

weekday = now.strftime("%A")
print(weekday)