select distinct t1.id, iif(t1.p_id is null, 'Root', iif(t2.id is null, 'Leaf', 'Inner')) type
from Tree t1
left join Tree t2 on t1.id = t2.p_id
