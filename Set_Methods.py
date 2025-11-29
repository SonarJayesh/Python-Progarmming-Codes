collection = {10,5,4,8,10}
collection2 = {10,3,4,8,7}

collection.add(2)
print(collection)

collection.add("Jayesh")

collection.remove(5)
print(collection)

print(collection.pop())
print(collection.pop())

print(collection.union(collection2)) #union of two sets 

print(collection.intersection(collection2))
collection.clear();
print(collection)



