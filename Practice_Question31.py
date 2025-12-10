#Write a function to print the elements of a list in a singlr line.(list is the paramenter)
 
cities = ["Mumbai","Pune","Nashik","Delhi","Shahada"]

def print_List(list):
    for item in cities:
        print(item, end=" ")


print_List(cities)