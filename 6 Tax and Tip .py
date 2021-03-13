#Tax and tip
#Ask for the primary cost of meal
a = float(input('Ask for cost of meal:'))
#Computing tax for the meal
tax = float(a * 5/100)
#Computing tip for the meal
tip = float(a * 18/100)
#Grand total of the meal
x = a + tip + tax
print('Tax for the respective meal=',tax)
print('Tip for the respective meal=',tip)
print('Grand total of the meal=',x)
