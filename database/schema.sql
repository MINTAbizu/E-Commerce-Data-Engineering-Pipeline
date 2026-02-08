
CREATE TABLE IF NOT EXISTS  orders(

    order_id  INT  PRIMARY KEY,
    customer_name  TEXT,
    producct  TEXT,
    category TEXT,
    price  NUMERIC,
    Quantity INT,
    order_date TIMESTAMP
    total_amount NUMERIC


);

-- CREATE TABLE IF NOT EXISTS  customers(

--     customer_id  INT  PRIMARY KEY,
--     customer_name  TEXT,
--     email  TEXT,
--     phone TEXT,
--     address  TEXT,
--     city TEXT,
--     state TEXT,
--     zip_code TEXT,
--     country TEXT
-- );
-- CREATE TABLE IF NOT EXISTS  products(

--     product_id  INT  PRIMARY KEY,
--     product_name  TEXT,
--     category TEXT,
--     price  NUMERIC,
--     stock_quantity INT,
--     supplier_id INT
-- );
-- CREATE TABLE IF NOT EXISTS  suppliers(

--     supplier_id  INT  PRIMARY KEY,
--     supplier_name  TEXT,
--     contact_name  TEXT,
--     address TEXT,
--     city TEXT,
--     state TEXT,
--     zip_code TEXT,
--     country TEXT,
--     phone TEXT
-- );

