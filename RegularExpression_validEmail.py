#Write a program to validate email addresses using regular expressions.

import re
email = input("Enter the email: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid Email")

else:
    print("Invalid Email")    