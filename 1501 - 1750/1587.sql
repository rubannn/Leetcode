select u.name, sum(t.amount) balance
from Transactions t
join users u on u.account = t.account
group by u.name
having sum(t.amount) > 10000
