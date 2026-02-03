#Implement a program to check password validity using regular expressions (conditions: 
#length, special characters, numbers, etc.).

import re

password = input("Enter password: ")

pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@#$]).{6,}$'

if re.match(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")

    