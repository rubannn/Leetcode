select u.user_id buyer_id, u.join_date, sum(iif(buyer_id is null, 0, 1)) orders_in_2019
from Users u
left join Orders o on o.buyer_id = u.user_id and year(order_date) = 2019
group by u.user_id, u.join_date
