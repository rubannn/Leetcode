select employee_id,
    iif(employee_id % 2 = 0 or name like 'M%', 0, salary) as bonus
from Employees
order by employee_id
