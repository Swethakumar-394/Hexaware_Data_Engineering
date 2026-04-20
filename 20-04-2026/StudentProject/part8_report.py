def write_final_report(combined):
    with open("report.txt", "w", encoding="utf-8") as file:
        file.write("Student Report\n")
        file.write("====================\n")

        for name, details in combined.items():
            file.write(
                f"{name} - Marks: {details['marks']} - Attendance: {details['attendance']:.1f}% "
                f"- Grade: {details['grade']}\n"
            )


def write_eligible_students(eligible_students):
    with open("eligible_students.txt", "w", encoding="utf-8") as file:
        for name in eligible_students:
            file.write(name + "\n")