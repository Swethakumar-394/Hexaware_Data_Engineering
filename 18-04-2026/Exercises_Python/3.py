#Student Marks Analyzer

students = {
    "Rahul": 85,
    "Sneha": 92,
    "Arjun": 78,
    "Priya": 88
}

topper = max(students, key=students.get)
average_marks = sum(students.values()) / len(students)

print("Topper:", topper, "-", students[topper])
print("Average marks:", average_marks)

print("Students scoring above 85:")
for name, marks in students.items():
    if marks > 85:
        print(name, "-", marks)
