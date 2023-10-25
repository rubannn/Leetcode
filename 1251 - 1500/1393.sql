with
buys as (
  select stock_name, operation, sum(price) sm
  from Stocks
  where operation = 'Buy'
  group by stock_name, operation
),
sells as (
  select stock_name, operation, sum(price) sm
  from Stocks
  where operation = 'Sell'
  group by stock_name, operation
)

select b.stock_name, s.sm - b.sm capital_gain_loss
from buys b
join sells s on s.stock_name = b.stock_name
