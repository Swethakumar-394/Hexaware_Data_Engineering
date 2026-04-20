def analyze_marks(students, calculate_average_marks):
    print("\nStudent Names and Marks:")
    for student in students:
        print(f"{student['name']} - {student['marks']}")

    highest = max(students, key=lambda student: student["marks"])
    lowest = min(students, key=lambda student: student["marks"])
    average = calculate_average_marks(students)

    python_students = []
    for student in students:
        if student["course"] == "Python":
            python_students.append(student)

    course_count = {}
    for student in students:
        course = student["course"]
        course_count[course] = course_count.get(course, 0) + 1

    print("\nHighest Marks Student:", highest["name"], "-", highest["marks"])
    print("Lowest Marks Student:", lowest["name"], "-", lowest["marks"])
    print("Average Marks:", average)

    print("\nStudents in Python Course:")
    for student in python_students:
        print(student["name"])

    print("Course Count:", course_count)

    return highest, lowest, average, python_students, course_count