with
u_partners as (
    select date_id, make_name, count(*) unique_partners
    from (select date_id,make_name,partner_id from DailySales group by date_id,make_name,partner_id) t
    group by date_id, make_name
),
u_leads as (
    select date_id, make_name, count(*) unique_leads
    from (select date_id,make_name,lead_id from DailySales group by date_id,make_name,lead_id) t
    group by date_id, make_name
)

select ul.*, up.unique_partners
from u_leads ul
left join u_partners up on up.date_id = ul.date_id and up.make_name = ul.make_name
