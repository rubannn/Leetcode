select iif((select salary SecondHighestSalary
          from (
            select salary, ROW_NUMBER() OVER(ORDER BY salary DESC) as rw
            from (select salary from Employee group by salary) q
          ) t
          where rw = 2) is not null,

          (select top 1 salary SecondHighestSalary
          from (
              select salary, ROW_NUMBER() OVER(ORDER BY salary DESC) as rw
              from (select salary from Employee group by salary) q
          ) t
          where rw = 2),
          null)  SecondHighestSalary
