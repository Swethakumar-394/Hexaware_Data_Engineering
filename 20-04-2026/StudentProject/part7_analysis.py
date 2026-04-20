def combine_marks_and_attendance(students, attendance_percentages, generate_grade):
    combined = {}

    for student in students:
        name = student["name"]
        combined[name] = {
            "marks": student["marks"],
            "attendance": attendance_percentages.get(name, 0),
            "course": student["course"],
            "grade": generate_grade(student["marks"])
        }

    return combined


def print_combined_structure(combined):
    print("\nFinal Combined Analysis:")
    for name, details in combined.items():
        print(
            f"{name} - Marks: {details['marks']} - Attendance: {details['attendance']:.1f}% - "
            f"Course: {details['course']} - Grade: {details['grade']}"
        )


def find_eligible_students(combined):
    eligible = []
    for name, details in combined.items():
        if details["marks"] >= 75 and details["attendance"] >= 80:
            eligible.append(name)
    return eligible


def find_students_needing_improvement(combined):
    improvement = []
    for name, details in combined.items():
        if details["marks"] < 75 or details["attendance"] < 80:
            improvement.append(name)
    return improvement