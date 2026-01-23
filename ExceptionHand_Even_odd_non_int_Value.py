#Implement a function to check if a number is even or odd and handle exceptions for non integer input.

try:
    num = int(input("Enter a Number: "))
    if num %2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd:")

except ValueError:
    print("Invalid Input ! Please Enter an Integer Value: ")            