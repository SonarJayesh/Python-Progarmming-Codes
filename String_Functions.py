#All String functions:-->

str1 = "!!!  jayesh Sonar at Met's Institute Nashik.   !!!"
print(len(str1))
print(str1.upper() )
print(str1.lower())
print(str1.title())
print(str1.capitalize())
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())
print(str1.capitalize())
print(str1.replace("Nashik","Aadgaon"))
print(str1.find("o"))
print(str1.count("e"))
print(str1.strip(","))
print(str1.startswith("at"))
print(str1.endswith("hik."))
print(str1.index("yes"))
print(str1.swapcase())
print(str1.isupper())
print(str1.islower())
print(str1.istitle())

str2 = ["I","am","Student"]
print(" ".join(str2))


str3 = "123ABC*@abc"
print(str3.isdigit())
print(str3.isalpha())
print(str3.isalnum())

str4 = "Python"
print(str4.center(10,'*'))
print(str4.encode())

str5 = "Jayeshß"
print(str5.casefold())

name = "Jayesh"
age = 20
print("My name is {} and I am {} years old.".format(name, age))
