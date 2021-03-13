#Units of Time (Again)
#asjking the number of seconds.
s = float(input("Enter the number ofseconds = "))
#Assigning d for days, h fro hours, m for minutes, s for seconds.
d = int(s // (24 * 60 * 60 )) 
s = (s % ( 24 * 60 * 60 ))
h = int(s // (60 * 60))
s = s % ( 60 * 60)
m = int(s // 60)
s = int(s % 60)
print('The equivalent amount of time in the form of %d:%02d:%02d:%02d is '%(d,h,m,s))
