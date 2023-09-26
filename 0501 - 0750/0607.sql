select sp.name
from SalesPerson sp
    left join Orders o on sp.sales_id = o.sales_id
    left join Company c on o.com_id = c.com_id
group by sp.name
having STRING_AGG(c.name, ',') not like '%RED%' or STRING_AGG(c.name, ',') is null
