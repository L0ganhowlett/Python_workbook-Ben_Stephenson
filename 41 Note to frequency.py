#41 Note to Frequency
#Askng the user of Name of note and number of Octave
x = input("Enter the name of octave: ")
y = int(input("Enter the number of octave = "))
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88
f = 0
if x == "C":
    f = f + (C4 / (2 ** (4 - y)))
    print("The frequency of note C"+str(y)+" is",f)
elif x == "D":
    f = f + (D4 / (2 ** (4 - y)))
    print("The frequency of note D"+str(y)+" is",f)  
elif x == "G":
    f = f + (G4 / (2 ** (4 - y)))
    print("The frequency of note G"+str(y)+" is",f)  
elif x == "E":
    f = f + (E4 / (2 ** (4 - y)))
    print("The frequency of note E"+str(y)+" is",f)  
elif x == "F":
    f = f + (F4 / (2 ** (4 - y)))
    print("The frequency of note F"+str(y)+" is",f)  
elif x == "A":
    f = f + (A4 / (2 ** (4 - y)))
    print("The frequency of note A"+str(y)+" is",f)  
elif x == "B":
    f = f + (B4 / (2 ** (4 - y)))
    print("The frequency of note B"+str(y)+" is",f)  

                            
    
