#Write a Python program to handle a FileNotFoundError while opening a file.

try:
    file = open("data.txt","r")
    print(file.read())

except FileNotFoundError:
    print("File Not Found")