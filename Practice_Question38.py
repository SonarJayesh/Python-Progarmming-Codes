#Write a function that replace all occurrence of "Java" with "python" in above file
def replace_Word():

    with open("C:\Jayesh Codding Language\Python Programming\Chapter7_File_Input_Output\demo.txt","r") as f:

        data = f.read()
    new_data = data.replace("Java","python")
    print(new_data)    

replace_Word()    