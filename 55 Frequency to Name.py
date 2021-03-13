#55: Frequency to Name
a=float(input("Enter the frequency of the wavelength:"))
if a<3*(pow(10,9)):
    print("Name of electromagnetic radiation is Radio waves.")
elif 3*(pow(10,9))<=a<3*(pow(10,12)):
    print("Name of electromagnetic radiation is Microwaves.")
elif 3*(pow(10,12))<=a<4.3*(pow(10,14)):
    print("Name of electromagnetic radiation is Infrared light.")
elif 4.3*(pow(10,14))<=a<7.5*(pow(10,14)):
    print("Name of electromagnetic radiation is Visible light.")
elif 7.5*(pow(10,14))<=a<3*(pow(10,17)):
    print("Name of electromagnetic radiation is Ultraviolet light.")
elif 3*(pow(10,17))<=a<3*(pow(10,19)):
    print("Name of electromagnetic radiation is X-rays.")
elif 3*(pow(10,19))<=a:
    print("Name of electromagnetic radiation is Gamma rays.")
