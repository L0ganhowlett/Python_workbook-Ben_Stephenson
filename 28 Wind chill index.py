# 28 Wind Chill
#Asking for air temperature and wind speed.
T = float(input('Enter the air temperature in celsius= '))
v = float(input('Enter the velocity of windin km/h = '))
x = round(13.12 * 0.6215 * T - 11.37 * v ** 0.16 + 0.3965 * T * v ** 0.16)
print('Wind chill index = ',x)


