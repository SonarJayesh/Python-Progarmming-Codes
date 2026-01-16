#To find sum of digit of a given Number.
n = int(input("Enter a numbers:"))
sum = 0
while n>0:
    rem = n%10
    sum =sum+rem
    n = int(n/10)
print("Sum of number= ",sum)    