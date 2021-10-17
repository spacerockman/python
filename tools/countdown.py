import datetime
# year = input("Year:")
# month = input("Month:")
# day = input("Day:")

now = datetime.datetime.now()
target_date = datetime.datetime(year=2021, month=12, day=7)

print(target_date - now)
