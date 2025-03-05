-- 1. Найти общую сумму заказов для каждого клиента
SELECT
    customer_id,
    SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id;

-- 2. Найти клиента с максимальной суммой заказов
SELECT
    customer_id,
    SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id
ORDER BY SUM(amount) DESC
LIMIT 1;

-- если несколько клиентов могут иметь одинаковую максимальную сумму
WITH customer_totals AS (
    SELECT
        customer_id,
        SUM(amount) AS total_amount
    FROM orders
    GROUP BY customer_id
)
SELECT *
FROM customer_totals
WHERE total_amount = (SELECT MAX(total_amount) FROM customer_totals);



-- 3. Найти количество заказов, сделанных в 2023 году
SELECT COUNT(id) AS order_count
FROM orders
WHERE EXTRACT(YEAR FROM order_date) = 2023;

-- 4. Найти среднюю сумму заказа для каждого клиента
SELECT
    customer_id,
    ROUND(AVG(amount), 2) AS average_order_amount
FROM orders
GROUP BY customer_id;