studentDict = {
    "name" : "Jayesh",
    "rollNo" : 63,
    "age" : 21,
    "college" : "Met's IOM BKC Nashik", 
    "percentage" : 82.49,
    "Exam Pass" : True,

    "subject" : {
        "python" : 84.54,
        "java" : 81.60,
        "cpp" : 79.40,
        "DS" : 85.04,

    }    
}

print(studentDict.keys(),"\n")

print(studentDict.values(),"\n")

print(studentDict.items(),"\n")

print(studentDict.get("Exam Pass"),"\n")

studentDict.update({"city":"Nashik"})
print(studentDict)