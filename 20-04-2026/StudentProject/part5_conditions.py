def show_pass_fail(students):
    print("\nPass / Fail Status:")
    for student in students:
        if student["marks"] >= 50:
            print(student["name"], "- Pass")
        else:
            print(student["name"], "- Fail")


def show_grades(students, generate_grade):
    print("\nGrades:")
    for student in students:
        grade = generate_grade(student["marks"])
        print(student["name"], "-", grade)


def students_above_80_and_85(students, attendance_percentages):
    result = []

    for student in students:
        name = student["name"]
        marks = student["marks"]
        attendance = attendance_percentages.get(name, 0)

        if marks > 80 and attendance > 85:
            result.append(name)

    print("\nStudents with Marks > 80 and Attendance > 85%:", result)
    return result