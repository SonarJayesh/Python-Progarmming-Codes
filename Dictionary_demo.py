studentDict = {
    "name" : "Jayesh",
    "rollNo" : 63,
    "age" : 21,
    "college" : "Met's IOM BKC Nashik", 
    "percentage" : 82.49,
    "Exam Pass" : True
}

print(type(studentDict),"\n")
print(studentDict,"\n")
print(studentDict["name"],studentDict["college"],"\n")
studentDict["percentage"]= 88.90
print(studentDict)