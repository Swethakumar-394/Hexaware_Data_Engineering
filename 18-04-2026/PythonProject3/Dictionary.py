#Dictionary

student = {
    "name": "Arjun",
    "age": 25,
    "course": "Python"
}

print(student)

#accessing the key value pairs
print(student["name"])
print(student["age"])
print(student["course"])

#accessing the key value pairs
#Using get #another syntax
print(student.get("name"))
print(student.get("age"))
print(student.get("course"))

#Add a new pair
student["city"] = "Bangalore"
print(student)