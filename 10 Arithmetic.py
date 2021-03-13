#Arithmetic
#Ask the values of integers a and b respectively
a = int(input('Enter the value of a = '))
b = int(input('Enter the value of b = '))
from math import log10
print(a, '+', b, '=',a + b)
print(a, '-', b, '=',a - b)
print(a, 'x', b, '=',a * b)
print(a, '/', b, '=',a / b)
print(a, '%', b, '=',a % b)
print('The base 10 logarithm of', a, 'is', log10(a))
print(a,'**',b , '=',a ** b)
