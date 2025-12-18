f = open("C:\Jayesh Codding Language\Python Programming\Chapter7_File_Input_Output\demo.txt","r")

data=f.read(7)
print(data)

line1 = f.readline()
print(line1)

line2 = f.readlines()
print(line2)

f.close()