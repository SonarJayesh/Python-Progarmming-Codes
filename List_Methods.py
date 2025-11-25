list = [2,5,8,1,7,3,6,9]


print(list)

list.append(10)
print("Append = ",list)

list.sort()
print("sorted Elements = ",list)

list.sort(reverse=True)
print("Sort and Reverse Elements = ",list)

list.reverse()
print("reverse Elements = ",list)

list.insert(3,4)
print("Insert of Index value = ",list)

list.remove(1)
print("Remove element of first occurrence",list)

list.pop(3)
print("pop remove",list)



listStr = ["i","e","a"]

print("\n\n",listStr,"\n")
listStr.append("u")
print("Append = ",listStr)

listStr.sort()
print("sorted Elements = ",listStr)

listStr.sort(reverse=True)
print("Sort and Reverse Elements = ",listStr)

listStr.reverse()
print("reverse Elements = ",listStr)

listStr.insert(3,"o")
print("Insert of Index value = ",listStr)