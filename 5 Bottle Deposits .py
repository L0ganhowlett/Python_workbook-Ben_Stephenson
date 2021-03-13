#Bottle deposits
#Asking for number of 1 litre bottles
a = int(input('Enter the number of 1 litre bottles:'))
#Asking for number of bottles bigger than 1 litre
b = int(input('Enter the number of bottles with capacity more than 1 litre:'))
#Deposit for1 litre bottle is 0.10$ and bigger bottle is 0.25$ respectively
refund = float(a * 0.10 + b * 0.25)
#Displaying result
print('Refund for containers=',refund,'$') 
