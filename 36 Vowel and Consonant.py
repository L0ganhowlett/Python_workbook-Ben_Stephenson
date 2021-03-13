#Vowel or Consonant
x = input("Enter the alphabet = ")
if x == str('a') or x ==  str('e') or x == str('i') or x == str('o') or x == str('u'):
    print("It is a vowel")
elif x == str('y'):
    print("y is sometimes a vowel and sometimes a consonant")
else:
    print(x,"is an consonant.")
