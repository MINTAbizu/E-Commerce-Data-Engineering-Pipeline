from sqlalchemy import create_engine

def load_data(df):
    print("📤 Loading data to PostgreSQL...")

    engine = create_engine(
        "postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/ecommerce_db"
    )

    df.to_sql(
        "orders",
        engine,
        if_exists="append",
        index=False
    )

    print("✅ Data loaded successfully")
