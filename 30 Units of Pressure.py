# 30 Units of Pressure
P = float(input('Enter the value of pressure in (kPa) = '))
x = P * 0.00014503 * 1000
y = P * 9.8692e-3
z = P * 7.50062
print('Pressure in pounds per inches = ',x,'Pounds per inches')
print('Presure in atmospheres = ',y,'atm')
print('Pressure in millimeters of mercury = ',z,'Torr')
