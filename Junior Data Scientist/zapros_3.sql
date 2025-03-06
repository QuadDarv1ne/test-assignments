SELECT SUM(i.price) as total_purchases
FROM orders o
JOIN items i ON o.item_id = i.item_id
WHERE o.user_id = 1;
