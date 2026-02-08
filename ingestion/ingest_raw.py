import pandas as pd 

import  sqlalchemy
import create_engine

engine =create_engine('postgresql://postgres:password@localhost:5432/ecommerce')

files = {
    "customers": "data/customers.csv",
    "orders": "data/orders.csv",
    "order_items": "data/order_items.csv",
    "products": "data/products.csv",
    "payments": "data/payments.csv",
}

for table_name, file_path in files.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, engine, schema='raw', if_exists='replace', index=False)

    print(f"Data from {file_path} has been ingested into the 'raw' schema as the '{table_name}' table.")