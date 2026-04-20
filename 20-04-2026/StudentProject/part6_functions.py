import json
import csv


def read_names(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]


def load_student_marks(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data["students"]


def load_attendance(filename):
    attendance = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["days_present"] = int(row["days_present"])
            row["total_days"] = int(row["total_days"])
            attendance.append(row)
    return attendance


def calculate_average_marks(students):
    total = 0
    for student in students:
        total += student["marks"]
    return total / len(students)


def calculate_attendance_percentage(days_present, total_days):
    return (days_present / total_days) * 100


def get_topper(students):
    return max(students, key=lambda student: student["marks"])


def generate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"