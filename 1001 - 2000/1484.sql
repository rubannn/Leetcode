select
sell_date, count(*) num_sold, STRING_AGG(product, ',') WITHIN GROUP( ORDER BY product ASC) products
from
(
    select sell_date, product
    from Activities
    group by sell_date, product
) t
group by sell_date
order by sell_date
