with
Em as (
  select em.employee_id, em.name , s.salary
  from Employees em
  left join Salaries s on s.employee_id = em.employee_id
),
sl as (
  select s.employee_id, em.name , s.salary
  from Salaries s
  left join Employees em on s.employee_id = em.employee_id
)

select t.employee_id
from (
  select * from Sl
  union all
  select * from em) t
where name is null or salary is null
order by employee_id
