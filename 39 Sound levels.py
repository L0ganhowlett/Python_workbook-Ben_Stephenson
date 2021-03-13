#39 Sound Levels
#Asking the decibel level of Noise
x = float(input("Enter the decibel level of noise = "))
if x == 130:
    print("Jackhammer.")
elif x == 106:
    print("Gas lawnmower.")
elif x == 70:
    print("Alarm clock.")
elif x <= 40 :
    print("Quiet room.")
elif  130 > x > 106:
    print("Jackhammer or gas lawnmower.")
elif 106 > x > 70:
    print("Gas lawnmower or alarm clock.")
elif 70 > x > 40:
    print("Alarm clock or quiet room.")
elif x > 130:
    print("Jackhammer")
