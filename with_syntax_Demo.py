with open("C:\Jayesh Codding Language\Python Programming\Chapter7_File_Input_Output\demo.txt","r") as f:
    Data = f.read()
    print(Data)


with open("C:\Jayesh Codding Language\Python Programming\Chapter7_File_Input_Output\demo.txt","w") as f:
    f.write("New Data")
    
