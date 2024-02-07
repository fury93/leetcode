# Write your MySQL query statement below
SELECT ROUND(SUM(order_occurrences*item_count) / SUM(order_occurrences), 2)
       as average_items_per_order
FROM Orders;
[object Object]
