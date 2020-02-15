import calendar
days_arr = ['Monday', 'Tuesday', 'Wednesday',
'Thursday', 'Friday', 'Saturday', 'Sunday']
date = input("Enter a date (dd/mm/yyyy): ")

# Seprate day, month and year
dd = int(date[:date.find('/')])
mm = int(date[date.find('/') + 1:date.find('/', date.find('/') + 1)])
yyyy = int(date[date.find('/', date.find('/') + 1) + 1:])

# Get day of week 
day_num = (calendar.weekday(yyyy, mm, dd))
day_name = days_arr[day_num]
print(day_name)