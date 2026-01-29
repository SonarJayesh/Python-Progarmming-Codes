#Write a program to create a list of fruits, add a new fruit, sort the list, and delete the last fruit.

fruit = ["Apple", "Mango", "Banana"]

fruit.append("Orange")
fruit.sort()
fruit.pop()
print(fruit)



# Dynamic

fruits = []
n = int(input("Enter the Number of Fruits"))
for i in range(n):
    fruit = input("Enter the Fruit Name: ")
    fruits.append(fruit)

new_fruit = input("Enter the Fruit Name to Add")
fruits.append(new_fruit)
fruits.sort()
fruits.pop()

print("Final Fruit List: ", fruits)