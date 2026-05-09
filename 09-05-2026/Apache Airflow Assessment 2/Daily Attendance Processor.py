from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def create_attendance_file():
    with open("/tmp/attendance.txt", "w") as file:
        file.write("Aarav,Present\n")
        file.write("Priya,Present\n")
        file.write("Rahul,Absent\n")
        file.write("Sneha,Present\n")
        file.write("Kiran,Absent\n")
        file.write("Ananya,Present\n")
        file.write("Vikram,Present\n")
        file.write("Meera,Absent\n")
        file.write("Farhan,Present\n")
        file.write("Divya,Present\n")

    print("Attendance file created")


def read_attendance_file():
    with open("/tmp/attendance.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        print(line.strip())


def count_total_students():
    with open("/tmp/attendance.txt", "r") as file:
        lines = file.readlines()

    total_students = len(lines)

    print(f"Total Students = {total_students}")


def count_present_students():
    present_count = 0

    with open("/tmp/attendance.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        name, status = line.strip().split(",")

        if status == "Present":
            present_count += 1

    print(f"Present Students = {present_count}")


def count_absent_students():
    absent_count = 0

    with open("/tmp/attendance.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        name, status = line.strip().split(",")

        if status == "Absent":
            absent_count += 1

    print(f"Absent Students = {absent_count}")


def calculate_attendance_percentage():
    total_students = 0
    present_students = 0

    with open("/tmp/attendance.txt", "r") as file:
        lines = file.readlines()

    total_students = len(lines)

    for line in lines:
        name, status = line.strip().split(",")

        if status == "Present":
            present_students += 1

    percentage = (present_students / total_students) * 100

    print(f"Attendance Percentage = {int(percentage)}%")


def list_absent_students():
    print("Absent Students List")

    with open("/tmp/attendance.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        name, status = line.strip().split(",")

        if status == "Absent":
            print(name)


def generate_attendance_report():
    total_students = 0
    present_students = 0
    absent_students = 0

    with open("/tmp/attendance.txt", "r") as file:
        lines = file.readlines()

    total_students = len(lines)

    for line in lines:
        name, status = line.strip().split(",")

        if status == "Present":
            present_students += 1
        else:
            absent_students += 1

    percentage = (present_students / total_students) * 100

    if percentage >= 75:
        status = "Good"
    else:
        status = "Needs Improvement"

    with open("/tmp/attendance_report.txt", "w") as file:
        file.write("Daily Attendance Report\n")
        file.write(f"Total Students = {total_students}\n")
        file.write(f"Present Students = {present_students}\n")
        file.write(f"Absent Students = {absent_students}\n")
        file.write(f"Attendance Percentage = {int(percentage)}%\n")
        file.write(f"Status = {status}\n")

    print("Attendance report generated")


with DAG(
    dag_id="daily_attendance_processor_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    create_attendance_file_task = PythonOperator(
        task_id="create_attendance_file",
        python_callable=create_attendance_file
    )

    read_attendance_file_task = PythonOperator(
        task_id="read_attendance_file",
        python_callable=read_attendance_file
    )

    count_total_students_task = PythonOperator(
        task_id="count_total_students",
        python_callable=count_total_students
    )

    count_present_students_task = PythonOperator(
        task_id="count_present_students",
        python_callable=count_present_students
    )

    count_absent_students_task = PythonOperator(
        task_id="count_absent_students",
        python_callable=count_absent_students
    )

    calculate_attendance_percentage_task = PythonOperator(
        task_id="calculate_attendance_percentage",
        python_callable=calculate_attendance_percentage
    )

    list_absent_students_task = PythonOperator(
        task_id="list_absent_students",
        python_callable=list_absent_students
    )

    generate_attendance_report_task = PythonOperator(
        task_id="generate_attendance_report",
        python_callable=generate_attendance_report
    )

    create_attendance_file_task >> read_attendance_file_task >> count_total_students_task >> count_present_students_task >> count_absent_students_task >> calculate_attendance_percentage_task >> list_absent_students_task >> generate_attendance_report_task
