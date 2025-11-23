#Write a progran to find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
num3 = int(input("Enter the Third Number: "))

if(num1 > num2 and num1 > num3):
    print(num1," First is Greater")
elif(num2>num3):
    print(num2," Second is largest")
else:
    print(num3," Thirs is largest")    