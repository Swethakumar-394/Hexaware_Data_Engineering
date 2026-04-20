def data_structures(students, attendance_percentages):
    marks_list = []
    for student in students:
        marks_list.append(student["marks"])

    print("\nMarks List:", marks_list)
    print("Highest Marks:", max(marks_list))
    print("Lowest Marks:", min(marks_list))
    print("Sum of Marks:", sum(marks_list))

    courses_tuple = tuple(student["course"] for student in students)
    print("\nCourses Tuple:", courses_tuple)

    courses_set = set(courses_tuple)
    print("Unique Courses Set:", courses_set)

    marks_dict = {}
    for student in students:
        marks_dict[student["name"]] = student["marks"]
    print("Student Marks Dictionary:", marks_dict)

    attendance_dict = {}
    for name, percentage in attendance_percentages.items():
        attendance_dict[name] = percentage
    print("Student Attendance Dictionary:", attendance_dict)

    return marks_list, courses_tuple, courses_set, marks_dict, attendance_dict