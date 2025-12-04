#Search for a number x in this tuple using loop
#[1,4,9,16,25,36,49,64,81,100]

tuple1 = [1,4,9,16,25,36,49,64,81,100]
num = int(input("Enter the Value for search on the tuple"))
index = 0
for i in tuple1:
    if(num == i):
        val = num
        print(val, "is found at :",index)
    index +=1
