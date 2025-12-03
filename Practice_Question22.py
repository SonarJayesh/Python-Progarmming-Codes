#Search for a number x in this tuple using loop
#tuple=(1,4,9,16,25,36,49,64,81,100).

tuple1 = (1,4,9,16,25,36,49,64,81,100)

num = int(input("Enter the No for finding into the tuple: "))
i = 0
while i< len(tuple1):
    
    if(num == tuple1[i]):

        print(num ," is available in tuple at Index of ",i)
    i +=1

