#Write a multithreading program where one thread calculates the square of numbers and another calculates the factorial.

import threading
import math

def square(n):
    print("Square:", n*n)

def factorial(n):
    print("Factorial:", math.factorial(n))

num = int(input("Enter number: "))

t1 = threading.Thread(target=square, args=(num,))
t2 = threading.Thread(target=factorial, args=(num,))

t1.start()
t2.start()

