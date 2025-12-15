f = open("C:\Jayesh Codding Language\Python Programming\Chapter7_File_Input_Output\demo.txt","r")

data = f.read() # open for reading(default)
print(data)
print(type(data))
f.close()
