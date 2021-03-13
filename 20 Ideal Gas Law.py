#20 Ideal Gas Law.
#Asking values of pressure(P),Volume(V) and Temperature(T).
#Value of Gas Constant(R) = 8.314 J/mol.K
P = float(input("Enter the value of Pressure = "))
V = float(input("Enter  the value of Volume = "))
T = float(input("Enter the value of Temperature in celsius = ")) + 273.15
#Number of moles(n)
print("The number of moles is n = ", P * V /(8.314 * T)," mol")


