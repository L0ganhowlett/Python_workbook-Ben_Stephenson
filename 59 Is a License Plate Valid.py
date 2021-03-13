#59: Is a License Plate Valid?
a = input("Enter license plate number:")
if a[:3].isupper() and a[3:].isnumeric() and len(a)==6:
    print("It is an old style license plate.")
elif a[:4].isnumeric() and a[4:].isupper() and len(a)==7:
    print("It is newer style of license plate.")
else:
    print("It is not valid for either style of license plate.")


    
