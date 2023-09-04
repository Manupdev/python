#Dates

from datetime import datetime

now = datetime.now()



timestamp = now.timestamp()

print(timestamp)

year_2024 = datetime(2024,1,1)

def print_date(date):
    print(now.day)
    print(now.year)
    print(now.hour)

print_date(now)

from datetime import time
current_time = time(21,6,0)

print(current_time.hour)

from datetime import date

current_date = date(2024,7,7)

print(current_date)

hoy = date.today()
print(hoy)


current_date = date(current_date.year+1, current_date.month, current_date.day)
print(current_date.year)


from datetime import timedelta
start_timedelta = timedelta(200,10,100, weeks=10)
end_timedelta = timedelta(300,100,100, weeks=12)

print(end_timedelta - start_timedelta)