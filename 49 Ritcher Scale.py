# 49 Ritcher Scale
a =  float(input("Enter the magnitude: "))
if a < 2.0:
    print("Magnitude of ",a," earthquake is considered Micro earthquake")
elif 2.0 <= a < 3.0:
    print("Magnitude of ",a," earthquake is considered Very minor earthquake")
elif 3.0 <= a < 4.0:
    print("Magnitude of ",a," earthquake is considered Minor earthquake")
elif 4.0 <= a < 5.0:
    print("Magnitude of ",a," earthquake is considered Light earthquake")
elif 5.0 <= a < 6.0:
    print("Magnitude of ",a," earthquake is considered Moderate earthquake")
elif 6.0 <= a < 7.0:
    print("Magnitude of ",a," earthquake is considered Strong earthquake")
elif 7.0 <= a < 8.0:
    print("Magnitude of ",a," earthquake is considered Major earthquake")
elif 8.0 <= a < 10.0:
    print("Magnitude of ",a," earthquake is considered Great earthquake")
elif 10.0 <= a:
    print("Magnitude of ",a," earthquake is considered Meteoric earthquake")


