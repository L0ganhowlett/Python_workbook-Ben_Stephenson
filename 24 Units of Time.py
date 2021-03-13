# 24 Units of Time.
# Asking for number of days, hour, minutes and seconds.
d = float(input("Enter the no=umber of days = "))
h = float(input("Enter the number of hours = "))
m = float(input("Enter the number of minutes = "))
s = float(input("Enter the number of seconds = "))
print('The total number of seconds = ',(d * 24 * 60 * 60) + (h * 60 * 60) + (m * 60) + s," seconds")
