from part1_students import analyze_students
from part2_marks import analyze_marks
from part3_attendance import analyze_attendance
from part4_datastructures import data_structures
from part5_conditions import show_pass_fail, show_grades, students_above_80_and_85
from part6_functions import (
    read_names,
    load_student_marks,
    load_attendance,
    calculate_average_marks,
    calculate_attendance_percentage,
    get_topper,
    generate_grade
)
from part7_analysis import (
    combine_marks_and_attendance,
    print_combined_structure,
    find_eligible_students,
    find_students_needing_improvement
)
from part8_report import write_final_report, write_eligible_students


def main():
    # Part 6 functions used throughout
    names = read_names("students.txt")
    students = load_student_marks("marks.json")
    attendance_data = load_attendance("attendance.csv")

    # Part 1
    total_entries, unique_names, name_count = analyze_students(names)

    # Part 2
    highest, lowest, average, python_students, course_count = analyze_marks(
        students, calculate_average_marks
    )

    # Part 3
    attendance_percentages, below_80, best_attendance = analyze_attendance(
        attendance_data, calculate_attendance_percentage
    )

    # Part 4
    marks_list, courses_tuple, courses_set, marks_dict, attendance_dict = data_structures(
        students, attendance_percentages
    )

    # Part 5
    show_pass_fail(students)
    show_grades(students, generate_grade)
    qualified_students = students_above_80_and_85(students, attendance_percentages)

    # Part 7
    combined = combine_marks_and_attendance(students, attendance_percentages, generate_grade)
    print_combined_structure(combined)

    eligible_students = find_eligible_students(combined)
    improvement_students = find_students_needing_improvement(combined)

    print("\nEligible Students for certification.:", eligible_students)
    print("Students Needing Improvement:", improvement_students)

    # Part 8
    write_final_report(combined)
    write_eligible_students(eligible_students)

    # Final Challenge
    topper = get_topper(students)

    print("\nFinal Console Output:")
    print("Topper:", topper["name"])
    print("Best Attendance:", best_attendance[0])
    print("Average Marks:", round(average, 1))
    print("Eligible Students:", ", ".join(eligible_students))
    print("Students Needing Improvement:", ", ".join(improvement_students))


if __name__ == "__main__":
    main()