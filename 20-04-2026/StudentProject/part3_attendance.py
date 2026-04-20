def analyze_attendance(attendance_data, calculate_attendance_percentage):
    print("\nAttendance Details:")

    attendance_percentages = {}

    for student in attendance_data:
        name = student["name"]
        days_present = student["days_present"]
        total_days = student["total_days"]

        percentage = calculate_attendance_percentage(days_present, total_days)
        attendance_percentages[name] = percentage

        print(f"{name} - Days Present: {days_present}, Total Days: {total_days}, Attendance: {percentage:.1f}%")

    below_80 = []
    for name, percentage in attendance_percentages.items():
        if percentage < 80:
            below_80.append(name)

    best_attendance = max(attendance_percentages.items(), key=lambda item: item[1])

    print("\nStudents Below 80% Attendance:", below_80)
    print("Best Attendance:", best_attendance)

    return attendance_percentages, below_80, best_attendance