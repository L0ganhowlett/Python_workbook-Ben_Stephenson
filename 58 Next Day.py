#58: Next Day
a=input("Enter the date:")
b=[1,3,5,7,8,10,12]
c=[4,6,9,11]
d=a.split('-')
year=int(d[0])
month=int(d[1])
date=int(d[2])
if year%400==0:
    x=True
elif year%100==0:
    x=False
elif year%4==0:
    x=True
else:
    x=False
if 1<=month<=12 and 1<=date<=31:
    if month in b:
        date+=1
        if date>31:
            month+=1
            date=1
            if month>12:
                year+=1
                month=1
    elif month in c:
        date+=1
        if date>30:
            month+=1
            date=1
    elif month==2:
        if x:
            date+=1
            if date>29:
                month+=1
                date=1
        else:
            date+=1
            if date>28:
                month+=1
                date=1
    print(year,"-",month,"-",date)
else:
    print("Invalid input")
                
    
    
    
    
    
