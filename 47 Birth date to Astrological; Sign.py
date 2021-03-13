#47 Birth Date to Astrological Sign
#Asking user to input day of birth and month.
x = int(input("Day of birth : "))
y = input("Enter the name of birth month : ")
if y == "January":
    if x <= 19:
        z = "Capricorn"
    elif 19 < x <= 31:
        z = "Aquarius"
if y == "February":
    if x <= 18:
        z = "Aquarius"
    elif 18 < x <= 29:
        z = "Pisces"
if y == "March":
    if x <= 20:
        z = "Pices"
    elif 20 < x <= 31:
        z = "Aries"
if y == "April":
    if x <= 19:
        z = "Aries"
    elif 19 < x <= 30:
        z = "Taurus"
if y == "May":
    if x <= 20:
        z = "Taurus"
    elif 20 < x <= 31:
        z = "Gemini"
if y == "June":
    if x <= 20:
        z = "Gemini"
    elif 20 < x <= 30:
        z = "Cancer"
if y == "July":
    if x <= 22:
        z = "Cancer"
    elif 22 < x <= 31:
        z = "Leo"
if y == "August":
    if x <= 22:
        z = "Leo"
    elif 22 < x <= 31:
        z = "Virgo"
if y == "Septemebr":
    if x <= 22:
        z = "Virgo"
    elif 22 < x <= 30:
        z = "Libra"
if y == "October":
    if x <= 22:
        z = "Libra"
    elif 22 < x <= 31:
        z = "Scorpio"
if y == "November":
    if x <= 21:
        z = "Scorpio"
    elif 21 < x <= 30:
        z = "Sagittarius"
if y == "December":
    if x <= 21:
        z = "Sagittarius"
    elif 21 < x <= 31:
        z = "Capricorn"
print("Astological sign is :",z)
