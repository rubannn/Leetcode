select e.name Employee
from Employee e
left join (select id, salary from Employee) em on em.id = e.managerid
where em.salary < e.salary and e.managerid is not null
