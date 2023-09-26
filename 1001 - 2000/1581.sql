select v.customer_id, count(*) count_no_trans
from Visits v
left join Transactions tr on v.visit_id = tr.visit_id
where tr.transaction_id is null
group by v.customer_id
