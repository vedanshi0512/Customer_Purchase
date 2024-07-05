import pandas as pd
from sqlalchemy import create_engine, text

# Load CSV file into a DataFrame
df = pd.read_csv('purchase_data_exe.csv')

df = df.drop(columns=["Unnamed: 7"])



# Rename columns to match the database schema
df.rename(columns={
    'value [USD]': 'value_usd',
    'date': 'date',
    'customer_id': 'customer_id',
    'product_category': 'product_category',
    'payment_method': 'payment_method',
    'time_on_site [Minutes]': 'time_on_site',
    'clicks_in_site': 'clicks_in_site',
    # 'Unnamed: 7': 'unnamed_7'
}, inplace=True)

if 'unnamed_7' in df.columns:
    df = df.drop(columns=['unnamed_7'])

# Create a connection to the PostgreSQL database
engine = create_engine('postgresql://postgres:123456@localhost:5432/customer_purchase_db1')
# def connect_to_database():
#     """Establishes a connection to the PostgreSQL database."""
#     engine = create_engine(f'postgresql://postgres:123456@localhost:5432/customer_purchase_db1')
#     return engine
def load_data(query):
    """Executes SQL query and returns results as a DataFrame."""
    # engine = connect_to_database()
    with engine.connect() as conn:
        result = conn.execute(text(query))  # Use text() function to execute SQL query
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
    return df
    # with engine.connect() as conn:
    #     result = conn.execute(query)
    #     df = pd.DataFrame(result.fetchall(), columns=result.keys())
    # return df

# Load data into the PostgreSQL table
df.to_sql('purchases', engine, if_exists='append', index=False)
print(df.head())
