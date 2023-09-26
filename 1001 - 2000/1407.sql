select name, travelled_distance
from
(
  select name, u.id, sum(isnull(distance, 0)) travelled_distance
  from Users u
  left join Rides r on r.user_id = u.id
  group by name, u.id
) tmp
order by travelled_distance desc, name
