#8 Widgets and Gizmos
#Asking number of widgets and gizmos from user for the respective order
a = int(input('Enter the number of widgets for the order:'))
b = int(input('Enter the number of gizmos for the  order:'))
#Assigning the variable c as weight of the widget and d as the weight of gizmos in grams respectively
c = 75
d = 112
#Weight of the order is given by the variable e
e = float(a*c + b*d)
print('The weight of your order is =',e,'g')
