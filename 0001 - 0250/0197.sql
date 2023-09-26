select w.id
from Weather w
where w.temperature > (select x.temperature from weather x where DATEDIFF (dd, convert(date, x.recorddate), convert(date, w.recorddate)) = 1)
