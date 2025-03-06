SELECT o.order_id, o.user_id, i.name, i.price
FROM orders o
JOIN items i ON o.item_id = i.item_id
WHERE i.price >= 3;
