#68: Parity Bits
a=input("Enter the 8 bits:")
while a!="":
    if len(a)!=8:
        print("Invalid input")
    else:
        b=a.count("1")
        if b%2==0:
            print("The parity bit should be 0.")
        else:
            print("The parity bit should be 1.")
    a=input("Enter 8 bits: ")        
    
