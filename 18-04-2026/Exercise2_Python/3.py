# Exercise 3 — JSON File (Student Dataset)

import json

with open("students.json", "r") as file:
    data = json.load(file)

students = data["students"]

print("All student names:")
for student in students:
    print(student["name"])

print("\nStudents enrolled in Python course:")
for student in students:
    if student["course"] == "Python":
        print(student["name"])

highest_marks_student = max(students, key=lambda x: x["marks"])
print("\nStudent with highest marks:")
print(highest_marks_student)

total_marks = 0
for student in students:
    total_marks += student["marks"]

average_marks = total_marks / len(students)
print("\nAverage marks:", average_marks)

course_count = {}
for student in students:
    course = student["course"]
    course_count[course] = course_count.get(course, 0) + 1

print("\nStudent count in each course:")
print(course_count)