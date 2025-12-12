#Write a recursive function to print all elements in a list.
def rec_list(list, idx):

    if(idx == len(list)):
    
        return
    
    print(list[idx])
    
    rec_list(list, idx+1)   

fruits = ["mango","litchi","apple","banana"]

rec_list(fruits,0)