#Write a function to find in which line of the file does the word "learning" occur first print -1  if word not found.

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("C:\Jayesh Codding Language\Python Programming\practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no +=1
        return -1
    
check_for_line()                