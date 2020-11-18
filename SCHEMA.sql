-- Create tables to hold information from imported csv files
CREATE TABLE departments (
	dept_no VARCHAR PRIMARY KEY,
	dept_name VARCHAR
);
-- NOT PULLING DATA<<<<
CREATE TABLE dept_emp (
	emp_no INT PRIMARY KEY,
	dept_no VARCHAR
);
DROP TABLE dept_emp
CREATE TABLE dept_manager (
	dept_no VARCHAR,
	emp_no INT
);

CREATE TABLE employees (
	emp_no INT PRIMARY KEY,
	emp_title_id VARCHAR,
	birth_date DATE,
	first_name VARCHAR,
	last_name VARCHAR,
	sex VARCHAR,
	hire_date DATE
);
CREATE TABLE salaries (
	emp_no INT PRIMARY KEY,
	salary INT
);
CREATE TABLE titles (
	table_id SERIAL PRIMARY KEY,
	title_id VARCHAR,
	title VARCHAR
);

-- Task one: List Employee (#, last name, first name, sex, salary)
SELECT e.emp_no, e.last_name, e.first_name, e.sex, s.salary
FROM employees e
JOIN salaries s
ON e.emp_no = s.emp_no;

-- Task two: List employees hired in 1986 (first name, last name, hire date)
SELECT  first_name, last_name, hire_date
FROM employees 
WHERE hire_date > '12/31/1985'
AND hire_date < '1/1/1987'
ORDER BY last_name;

-- Task three: List managers by department (dept number, dept name, manager's employee number, last name, first name)
SELECT d.dept_no, d.dept_name, dm.emp_no, e.last_name, e.first_name
FROM departments d
RIGHT JOIN dept_manager dm
ON d.dept_no = dm.dept_no
LEFT JOIN employees e
ON dm.emp_no = e.emp_no

-- Task four: List dept of each employee ( dept number, last name, first name, dept name)
SELECT de.dep_no,e.last_name, e.first_name
-- de.dep_no, d.dept_name, e.last_name, e.first_name
FROM employees e
RIGHT JOIN dept_emp de
ON e.emp_no = de.emp_no
JOIN departments d
ON d.dept_no = de.dep_no

SELECT *
From dept_emp


SELECT *
FROM dept_manager
-- Task five: List employees first name "Hercules", last name "B" (first name, last name, sex)

-- Task six: List all employees in Sales dept (employee number, last name, first name, dept. name)

-- Task seven: List all employees in Sales and Development dept. (emp number, last name, first name, dept name)

-- Task eight: List in descending order freqency count of employee last names 
-- (i.e. how many employees share each last name.)

-- BONUS: import into pandas AS A DATABASE, generate a visualization - HISTOGRAM of most common salary ranges for employees
-- BONUS: create a bar chart of average salary by title.




-- -- CODE to VIEW
-- SELECT *
-- FROM employees
-- ORDER BY emp_no

-- -- CODE TO RESET
-- DROP TABLE departments
-- DROP TABLE dept_emp
-- DROP TABLE dept_manager
-- DROP TABLE employees
-- DROP TABLE salaries
-- DROP TABLE titles