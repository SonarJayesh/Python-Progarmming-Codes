#To check if the entered number is Prime or not.
n = int(input("Enter the Number:"))
for i in range(2,n+1):
    if n%i ==0:
        break
if i==n:
    print(n,"is a Prime Number:")
else:
    print(n,"is Not a prime Number")    