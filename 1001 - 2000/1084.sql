select product_id, product_name
from
(
  select p.product_id, p.product_name,  iif(sale_date >= '2019-01-01' and sale_date <= '2019-03-31', 1, 0) as checkData
  from Sales s
  left join product p on p.product_id = s.product_id
  group by p.product_id, p.product_name, s.sale_date
) q
group by product_id, product_name
having sum(q.checkData) = count(*)
