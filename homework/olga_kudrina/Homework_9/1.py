import datetime

calendar = 'Jan 15, 2023 - 12:05:33'
calendar_py = datetime.datetime.strptime(calendar, '%b %d, %Y - %X')
calendar_month = calendar_py.strftime('Month: %B')
print(calendar_month)
calendar_time = calendar_py.strftime('\"%d.%m.%Y, %H:%M\"')
print(calendar_time)
