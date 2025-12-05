# Write a program to find the factorial of first n number(using  for)

num = int(input("Enter the Factorial number"))
fact = 1

for i in range(1,num+1):
    fact *= i

print("Factorial of ",num, " = ",fact)