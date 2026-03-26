CREATE DATABASE company_training;

USE company_training;

CREATE TABLE employees (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(100),
department VARCHAR(50),
city VARCHAR(50)
);

CREATE TABLE projects (
project_id INT PRIMARY KEY,
emp_id INT,
project_name VARCHAR(100),
project_budget DECIMAL(12,2),
project_status VARCHAR(50)
);

INSERT INTO employees VALUES
(1, 'Rohan Mehta', 'IT', 'Hyderabad'),
(2, 'Sneha Iyer', 'IT', 'Bangalore'),
(3, 'Kiran Patel', 'Finance', 'Mumbai'),
(4, 'Ananya Das', 'HR', NULL),
(5, 'Rahul Sharma', 'IT', 'Delhi'),
(6, NULL, 'Marketing', 'Chennai');

INSERT INTO projects VALUES
(101, 1, 'AI Chatbot', 120000, 'Active'),
(102, 1, 'ML Prediction', 90000, 'Active'),
(103, 2, 'Data Warehouse', 150000, 'Active'),
(104, 3, 'Financial Dashboard', 80000, 'Completed'),
(105, NULL, 'Website Revamp', 60000, 'Pending'),
(106, 8, 'Mobile App', 100000, 'Active');

-- Exercise 1

SELECT 
employees.emp_name,
projects.project_name,
projects.project_budget
FROM employees
INNER JOIN projects
ON employees.emp_id = projects.emp_id;

-- Exercise 2

SELECT 
employees.emp_name,
projects.project_name
FROM employees
LEFT JOIN projects
ON employees.emp_id = projects.emp_id;

-- Exercise 3

SELECT 
employees.emp_name,
projects.project_name
FROM employees
RIGHT JOIN projects
ON employees.emp_id = projects.emp_id;

-- Exercise 4

SELECT 
employees.emp_name,
projects.project_name,
projects.project_budget
FROM employees
LEFT JOIN projects
ON employees.emp_id = projects.emp_id UNION
SELECT 
employees.emp_name,
projects.project_name,
projects.project_budget
FROM employees
RIGHT JOIN projects
ON employees.emp_id = projects.emp_id;

-- Exercise 5

SELECT 
employees.emp_id,
employees.emp_name,
employees.department,
employees.city,
projects.project_id,
projects.project_name,
projects.project_budget,
projects.project_status
FROM employees
LEFT JOIN projects
ON employees.emp_id = projects.emp_id 
UNION
SELECT 
employees.emp_id,
employees.emp_name,
employees.department,
employees.city,
projects.project_id,
projects.project_name,
projects.project_budget,
projects.project_status
FROM employees
RIGHT JOIN projects
ON employees.emp_id = projects.emp_id;


-- Exercise 5

SELECT *
FROM employees
CROSS JOIN projects;

-- Exercise 6

SELECT 
employees.emp_name,
employees.department,
projects.project_name,
projects.project_budget,
projects.project_status
FROM employees
INNER JOIN projects
ON employees.emp_id = projects.emp_id
WHERE employees.department = 'IT';

-- Exercise 7

SELECT 
employees.emp_name,
projects.project_name,
projects.project_budget,
projects.project_status
FROM employees
INNER JOIN projects
ON employees.emp_id = projects.emp_id
WHERE projects.project_budget > 100000;


-- Exercise 8 

SELECT 
employees.emp_name,
employees.city,
projects.project_name
FROM employees
INNER JOIN projects
ON employees.emp_id = projects.emp_id
WHERE employees.city = 'Hyderabad';

-- 3 — Join with Aggregate Functions

-- Exercise 9

SELECT 
employees.emp_name,
COUNT(projects.project_id) AS total_projects
FROM employees
LEFT JOIN projects
ON employees.emp_id = projects.emp_id
GROUP BY employees.emp_name;

-- Exercise 10

SELECT 
employees.emp_name,
SUM(projects.project_budget) AS total_project_budget
FROM employees
LEFT JOIN projects
ON employees.emp_id = projects.emp_id
GROUP BY employees.emp_name;

-- Exercise 11

SELECT 
employees.department,
AVG(projects.project_budget) AS avg_project_budget
FROM employees
LEFT JOIN projects
ON employees.emp_id = projects.emp_id
GROUP BY employees.department;

-- 4 — GROUP BY

-- Exercise 12
SELECT 
employees.department,
COUNT(projects.project_id) AS total_projects
FROM employees
LEFT JOIN projects
ON employees.emp_id = projects.emp_id
GROUP BY employees.department;

-- Exercise 13

SELECT 
employees.department,
SUM(projects.project_budget) AS total_budget
FROM employees
LEFT JOIN projects
ON employees.emp_id = projects.emp_id
GROUP BY employees.department;

-- Exercise 14

SELECT 
city,
COUNT(emp_id) AS total_employees
FROM employees
GROUP BY city;

-- 5 — HAVING

-- Exercise 15

SELECT 
employees.emp_name,
COUNT(projects.project_id) AS total_projects
FROM employees
LEFT JOIN projects
ON employees.emp_id = projects.emp_id
GROUP BY employees.emp_name
HAVING COUNT(projects.project_id) > 1;

-- Exercise 16

SELECT 
employees.department,
SUM(projects.project_budget) AS total_budget
FROM employees
LEFT JOIN projects
ON employees.emp_id = projects.emp_id
GROUP BY employees.department
HAVING SUM(projects.project_budget) > 150000;

-- Exercise 17

SELECT 
employees.emp_name,
SUM(projects.project_budget) AS total_project_budget
FROM employees
LEFT JOIN projects
ON employees.emp_id = projects.emp_id
GROUP BY employees.emp_name
HAVING SUM(projects.project_budget) > 100000;

-- 6 — Capstone Query

SELECT 
employees.emp_name,
employees.department,
SUM(projects.project_budget) AS total_project_budget
FROM employees
LEFT JOIN projects
ON employees.emp_id = projects.emp_id
GROUP BY employees.emp_name, employees.department
HAVING SUM(projects.project_budget) > 100000
ORDER BY total_project_budget DESC;

