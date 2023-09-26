with
customer_count as (
  select customer_number, count(*) count from orders group by customer_number
)

select customer_number
from customer_count
where count = (select max(count) from customer_count)
