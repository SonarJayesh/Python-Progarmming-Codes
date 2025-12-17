#Search if the wod "Learning" exist in the file or not.
word = "learning"
with open("C:\Jayesh Codding Language\Python Programming\practice.txt","r") as f:
    data = f.read()
    if(data.find(word) !=1):
        print("Found")
    else:
        print("Not Found")    
