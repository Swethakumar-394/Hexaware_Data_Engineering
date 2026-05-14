CREATE DATABASE retail_sales_db;
USE retail_sales_db;

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    cost DECIMAL(10,2)
);

CREATE TABLE stores (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(100),
    region VARCHAR(50)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_name VARCHAR(100),
    designation VARCHAR(50),
    store_id INT,
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    store_id INT,
    quantity INT,
    sale_date DATE,
    discount DECIMAL(5,2),
    returns INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

INSERT INTO products VALUES
(1,'Laptop','Electronics',60000,50000),
(2,'Mobile','Electronics',25000,18000),
(3,'Shoes','Fashion',3000,1500),
(4,'Watch','Accessories',5000,3000),
(5,'Headphones','Electronics',2000,1200);

INSERT INTO stores VALUES
(1,'Chennai Store','South'),
(2,'Bangalore Store','South'),
(3,'Mumbai Store','West'),
(4,'Delhi Store','North'),
(5,'Hyderabad Store','South');

INSERT INTO employees(employee_name,designation,store_id) VALUES
('Rahul','Manager',1),
('Anitha','Sales Executive',2),
('Kiran','Cashier',3),
('Meena','Manager',4),
('Arjun','Sales Executive',5);

INSERT INTO sales VALUES
(1,1,1,2,'2026-05-01',10,0),
(2,2,2,5,'2026-05-02',5,1),
(3,3,3,10,'2026-05-03',15,2),
(4,4,4,4,'2026-05-04',8,0),
(5,5,5,12,'2026-05-05',6,1);

SELECT * FROM sales;

UPDATE sales
SET quantity = 7
WHERE sale_id = 2;

DELETE FROM sales
WHERE sale_id = 5;

DELIMITER //

CREATE PROCEDURE GetDailySales(
    IN p_store_id INT,
    IN p_date DATE
)
BEGIN
    SELECT
        s.store_name,
        sa.sale_date,
        SUM(sa.quantity * p.price) AS total_sales
    FROM sales sa
    JOIN products p ON sa.product_id = p.product_id
    JOIN stores s ON sa.store_id = s.store_id
    WHERE sa.store_id = p_store_id
    AND sa.sale_date = p_date
    GROUP BY s.store_name, sa.sale_date;
END //

DELIMITER ;

CALL GetDailySales(1, '2026-05-01');

CREATE INDEX idx_product
ON products(product_name);

CREATE INDEX idx_region
ON stores(region);
