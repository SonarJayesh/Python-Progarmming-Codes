#Write a Program to ask user to enter names of their 3 favorite movies & store them in a list.
movies = []

first = input("Enter Your Favorite First Movies Names:")
movies.append(first)

second = input("Enter Your Favorite Second Movies Names:")
movies.append(second)

movies.append(input("Enter Your Favorite Thirs Movies Names:"))

print(movies)