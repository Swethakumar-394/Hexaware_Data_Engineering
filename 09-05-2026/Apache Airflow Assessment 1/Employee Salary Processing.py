from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def create_employee_file():
    with open("/tmp/employees.txt", "w") as file:
        file.write("Rahul,45000\n")
        file.write("Sneha,52000\n")
        file.write("Amit,61000\n")
        file.write("Priya,47000\n")
        file.write("Kiran,39000\n")
    print("Employee file created successfully")


def read_employee_data():
    with open("/tmp/employees.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        print(line.strip())


def calculate_salary_expense():
    total_salary = 0

    with open("/tmp/employees.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        name, salary = line.strip().split(",")
        total_salary += int(salary)

    print(f"Total Salary Expense = {total_salary}")


def find_highest_salary():
    highest_salary = 0
    highest_employee = ""

    with open("/tmp/employees.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        name, salary = line.strip().split(",")
        salary = int(salary)

        if salary > highest_salary:
            highest_salary = salary
            highest_employee = name

    print(f"Highest Salary = {highest_salary}")
    print(f"Employee = {highest_employee}")


def generate_salary_report():
    total_salary = 0
    total_employees = 0

    with open("/tmp/employees.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        name, salary = line.strip().split(",")
        total_salary += int(salary)
        total_employees += 1

    with open("/tmp/salary_report.txt", "w") as file:
        file.write("Employee Salary Report\n")
        file.write(f"Total Employees = {total_employees}\n")
        file.write(f"Total Salary Expense = {total_salary}\n")
        file.write("Status = Processed Successfully\n")

    print("Salary report generated successfully")
    print(f"Total Employees = {total_employees}")
    print(f"Total Salary Expense = {total_salary}")
    print("Status = Processed Successfully")


with DAG(
    dag_id="employee_salary_processing_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    create_employee_file_task = PythonOperator(
        task_id="create_employee_file",
        python_callable=create_employee_file
    )

    read_employee_data_task = PythonOperator(
        task_id="read_employee_data",
        python_callable=read_employee_data
    )

    calculate_salary_expense_task = PythonOperator(
        task_id="calculate_salary_expense",
        python_callable=calculate_salary_expense
    )

    find_highest_salary_task = PythonOperator(
        task_id="find_highest_salary",
        python_callable=find_highest_salary
    )

    generate_salary_report_task = PythonOperator(
        task_id="generate_salary_report",
        python_callable=generate_salary_report
    )

    create_employee_file_task >> read_employee_data_task >> calculate_salary_expense_task >> find_highest_salary_task >> generate_salary_report_task
