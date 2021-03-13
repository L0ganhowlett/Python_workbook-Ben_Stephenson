#60: Roulette Payouts
import random
x=random.randint(0,38)
a=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
if 0<x<37:
    print("The spin resulted in",x,"...")
    print("Pay",x)
elif x==0:
    print("Pay 0")
else:
    print("Pay 00")
if x in a and x!=0 and x!=37:
    print("Pay Red")
elif x!=0 and x!=37:
    print("Pay Black")
if x%2==0 and x!=0 and x!=37:
    print("Pay Even")
elif x!=0 and x!=37:
    print("Pay Odd")
if 1<=x<=18 and x!=0 and x!=37:
    print("Pay 1 to 18")
elif 19<=x<=36 and x!=0 and x!=37:
    print("Pay 19 to 36")
    

