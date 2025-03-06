SELECT
    EXTRACT(QUARTER FROM o.order_date) as quarter,
    SUM(i.price) as total_purchase,
    AVG(i.price) as average_purchase
FROM orders o
JOIN items i ON o.item_id = i.item_id
GROUP BY EXTRACT(QUARTER FROM o.order_date);
