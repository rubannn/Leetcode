select activity_date day, count(*) active_users
from (
  select user_id, activity_date
  from Activity
  group by user_id, activity_date) t
group by activity_date
having convert(date, '2019-07-27') >= convert(date, activity_date)
        and DATEDIFF (dd, convert(date, activity_date), convert(date, '2019-07-27')) < 30
