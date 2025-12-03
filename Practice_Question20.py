#Print the multiplication table of a number.

n = int(input("Enter the Multiplication table of a number"))

i = 1
while i <= 10:
    mul = n*i
    print(n,"*",i," =",mul) 
    i +=1