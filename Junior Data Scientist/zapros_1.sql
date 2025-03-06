SELECT item_id, name, price
FROM (
    SELECT item_id, name, price, update_date,
           ROW_NUMBER() OVER (PARTITION BY item_id ORDER BY update_date DESC) as rn
    FROM items
    WHERE update_date <= '2020-06-01'
) subquery
WHERE rn = 1;
