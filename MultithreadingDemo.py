#Implement multithreading where one thread prints squares of numbers and another prints cubes.

import threading

def square():
    for i in range(1,6):
        print("square: ",i*i)

def cube():
    for i in range(1,6):
        print("Cube: ",i*i*i)

t1 = threading.Thread(target=square)
t2 = threading.Thread(target=cube)

t1.start()
t2.start()

