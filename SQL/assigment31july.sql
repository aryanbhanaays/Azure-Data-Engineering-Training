/* Assignment 2. Write a query to display the employees whose firstname starts with 
'Y' and ends with 'n' from employees table */
SELECT * FROM employees 
WHERE employees.first_name LIKE 'Y%n';


-- Assignment 3. Write a query to display the emp_no and salary increased by 30% from salaries table.
-- Query
SELECT emp_no, salary * 1.30 AS increased_salary
FROM salaries;

-- Assignment 4 : Write a query to display unique titles from titles table.
--Query
SELECT DISTINCT title FROM titles;
