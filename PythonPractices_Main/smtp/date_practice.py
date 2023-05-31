import datetime as dt

now = dt.datetime.now()
print(now)
year = now.year
month = now.month
day = now.day
weekday = now.weekday()
print(f"{year},{month}")

# create date
date_of_birth = dt.datetime(year=1995, month=12, day=4)
print(date_of_birth)