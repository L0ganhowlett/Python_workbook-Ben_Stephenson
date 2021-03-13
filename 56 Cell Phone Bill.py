#56: Cell Phone Bill
a=float(input("Enter the number of minutes:"))
b=float(input("Enter the number of text messages:"))
if a<50 and b<50:
    baseCharge=round(15,2)
else:
    baseCharge=round((15+(a-50)*0.25+(b-50)*0.15),2)
print("Base charge:$",baseCharge)
print("911 fee:$ 0.44")
print("Tax:$",round(0.05*(baseCharge+0.44),2))
print("Total bill:$",round((baseCharge + 0.44+0.05*(baseCharge+0.44)),2))

