select q.event_day day, q.emp_id, sum(q.total_time) total_time
from (select
        event_day,
        emp_id,
        convert(int, out_time) - convert(int, in_time) as total_time
      from Employees) q
group by q.event_day, q.emp_id
