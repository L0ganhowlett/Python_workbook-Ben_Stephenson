#Compound interest
#Ask for the deposited amount in savings account
a = float(input('Enter the deposited amount in savings account:'))
N = int(input('Account balance status after how many years = '))
for i in range (1,N + 1):
    x = float((a * 4/100) + a)
    a = x
    print('The total amount after ',i,' years is:',x,u"\u20B9")
