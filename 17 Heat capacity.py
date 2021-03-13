#17 Heat Capacity
#Asking for masss of water.
m = float(input("Enter the mass of water in grams = "))
T = float(input("Enter the temperature change in degree celsius = "))
C = 4.186 * (2.7777e-7)
q = m * T * C
print("Total energy required to raise ",m," grams of a material by ",T," degrees Celsius is ",q," kilowatt-hour")
cost = (8.9 * q) / 240 
print("Cost of electricity for boiling water for a cup of coffee is ",cost," cents")

