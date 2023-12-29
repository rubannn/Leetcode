select p.product_name, sum(o.unit) unit
from Products p
join Orders o on o.product_id = p.product_id
group by p.product_name, month(o.order_date), year(o.order_date)
having month(o.order_date) = 2 and year(o.order_date) = 2020 and sum(o.unit) >= 100
