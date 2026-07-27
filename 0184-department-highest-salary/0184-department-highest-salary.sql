# Write your MySQL query statement below
select d.name as Department ,e.name as Employee,e.salary AS Salary from Employee e
join Department d on e.departmentId = d.id
join (select departmentId,MAX(salary) maxSalary from Employee group by departmentId)
as salary
ON e.departmentId = salary.departmentId
AND e.salary = salary.maxSalary