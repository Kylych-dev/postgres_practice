``` sql
psql -U postgres -h localhost

postgres=# CREATE DATABASE products
postgres-# ;
CREATE DATABASE
postgres=# CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL
);
CREATE TABLE
postgres=# INSERT INTO orders (customer_id, order_date, amount) VALUES
(1, '2023-01-15', 150.00),
(2, '2023-05-23', 200.50),
(1, '2023-08-11', 300.00),
(3, '2023-10-04', 450.75),
(2, '2023-12-10', 125.30);
INSERT 0 5
postgres=# exit
```

``` sql
psql -U postgres -h localhost

\c products

INSERT INTO orders (customer_id, order_date, amount)
VALUES
(1, '2023-01-15', 120.50),
(2, '2023-02-20', 300.75),
(1, '2023-03-10', 150.00),
(3, '2023-04-05', 90.00),
(2, '2023-05-15', 250.00);

```


``` sql
psql -U postgres -h localhost -d products -f task_3/query_script.sql
```


## Результаты SQL-запросов

### 1. Общая сумма заказов для каждого клиента:

| customer_id | total_amount |
|-------------|--------------|
| 3           | 90.00        |
| 2           | 550.75       |
| 1           | 270.50       |

### 2. Клиент с максимальной суммой заказов:

| customer_id |
|-------------|
| 2           |

### 3. Количество заказов, сделанных в 2023 году:

| order_count |
|-------------|
| 5           |

### 4. Средняя сумма заказа для каждого клиента:

| customer_id | average_order_amount |
|-------------|----------------------|
| 3           | 90.0000000000000000   |
| 2           | 275.3750000000000000  |
| 1           | 135.2500000000000000  |


