select x.*
from Products
CROSS APPLY (VALUES
        (product_id, 'store1', store1),
        (product_id, 'store2', store2),
        (product_id, 'store3', store3)
    ) x (product_id, store, price)
where x.price is NOT NULL
