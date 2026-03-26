CREATE DATABASE capstone_sql;

USE capstone_sql;

CREATE TABLE students (
 student_id INT PRIMARY KEY,
 student_name VARCHAR(100),
 city VARCHAR(50),
 age INT
);

CREATE TABLE enrollments (
 enrollment_id INT PRIMARY KEY,
 student_id INT,
 course_name VARCHAR(100),
 trainer VARCHAR(100),
 fee DECIMAL(10,2)
);

INSERT INTO students VALUES
(1,'Aarav Sharma','Hyderabad',22),
(2,'Priya Reddy','Bangalore',23),
(3,'Rahul Verma','Mumbai',24),
(4,'Sneha Kapoor',NULL,21),
(5,'Vikram Singh','Chennai',25),
(6,NULL,'Delhi',22);

INSERT INTO enrollments VALUES
(101,1,'MySQL','Abdullah Khan',5000),
(102,1,'Python','Abdullah Khan',7000),
(103,2,'Power BI','Kiran',6000),
(104,3,'Azure Data Factory','Sneha',8000),
(105,NULL,'Excel','Rohan',3000),
(106,8,'Databricks','Ananya',9000);

-- Exercise 1

SELECT 
students.student_name,
enrollments.course_name
FROM students
INNER JOIN enrollments
ON students.student_id = enrollments.student_id;

-- Exercise 2

SELECT 
students.student_name,
enrollments.course_name
FROM students
LEFT JOIN enrollments
ON students.student_id = enrollments.student_id;

-- Exercise 3

SELECT 
students.student_name,
enrollments.course_name
FROM students
RIGHT JOIN enrollments
ON students.student_id = enrollments.student_id;

-- Exercise 4

SELECT *
FROM students
LEFT JOIN enrollments
ON students.student_id = enrollments.student_id
UNION
SELECT *
FROM students
RIGHT JOIN enrollments
ON students.student_id = enrollments.student_id;

-- Exercise 5

SELECT *
FROM students
CROSS JOIN enrollments;

-- Exercise 6

SELECT 
students.student_name,
students.city,
enrollments.course_name
FROM students
INNER JOIN enrollments
ON students.student_id = enrollments.student_id
WHERE students.city = 'Hyderabad';

-- Exercise 7

SELECT 
enrollments.course_name,
enrollments.fee
FROM students
INNER JOIN enrollments
ON students.student_id = enrollments.student_id
WHERE enrollments.fee > 6000;

-- Exercise 8

SELECT 
students.student_name,
COUNT(enrollments.enrollment_id) AS total_courses
FROM students
LEFT JOIN enrollments
ON students.student_id = enrollments.student_id
GROUP BY students.student_name;

-- Exercise 9

SELECT 
students.student_name,
SUM(enrollments.fee) AS total_fee
FROM students
LEFT JOIN enrollments
ON students.student_id = enrollments.student_id
GROUP BY students.student_name;

-- Exercise 10

SELECT 
students.student_name,
COUNT(enrollments.enrollment_id) AS total_courses
FROM students
LEFT JOIN enrollments
ON students.student_id = enrollments.student_id
GROUP BY students.student_name
HAVING COUNT(enrollments.enrollment_id) > 1;

-- Exercise 11

SELECT 
enrollments.trainer,
SUM(enrollments.fee) AS total_fee
FROM enrollments
GROUP BY enrollments.trainer
HAVING SUM(enrollments.fee) > 10000;

-- Exercise 12

SELECT 
city,
COUNT(student_id) AS total_students
FROM students
GROUP BY city
HAVING COUNT(student_id) > 1;

-- Final Capstone Query

SELECT 
students.student_name,
students.city,
SUM(enrollments.fee) AS total_fee_paid
FROM students
LEFT JOIN enrollments
ON students.student_id = enrollments.student_id
GROUP BY students.student_name, students.city
HAVING SUM(enrollments.fee) > 5000
ORDER BY total_fee_paid DESC;

