#write a function to find the factorial of n. (n is the parameter)

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    print("Factorial of",n," = ",fact)

factorial(5)