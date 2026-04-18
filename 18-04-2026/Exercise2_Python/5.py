# Exercise 5 — CSV File (Employee Dataset)

import csv

employees = []

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["salary"] = int(row["salary"])
        employees.append(row)

print("All employee names:")
for emp in employees:
    print(emp["name"])

print("\nEmployees in IT department:")
for emp in employees:
    if emp["department"] == "IT":
        print(emp["name"])

total_salary = 0
for emp in employees:
    total_salary += emp["salary"]

average_salary = total_salary / len(employees)
print("\nAverage salary:", average_salary)

highest_salary_employee = max(employees, key=lambda x: x["salary"])
print("\nHighest salary employee:")
print(highest_salary_employee)

department_count = {}
for emp in employees:
    dept = emp["department"]
    department_count[dept] = department_count.get(dept, 0) + 1

print("\nEmployees count by department:")
print(department_count)