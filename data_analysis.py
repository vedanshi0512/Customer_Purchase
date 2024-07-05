import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Constants for database connection
DB_USER = 'postgres'
DB_PASSWORD = '123456'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'customer_purchase_db1'

# Create a connection to the PostgreSQL database
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Query the database and load data into a DataFrame
query = """
    SELECT 
        customer_id, 
        COUNT(*) AS total_purchases, 
        SUM(value_usd) AS total_value
    FROM 
        purchases
    GROUP BY 
        customer_id;
"""
df = pd.read_sql(query, engine)

# Sort DataFrame by customer_id for better line plot representation
df.sort_values(by='customer_id', inplace=True)

# Plotting total purchases per customer as a line chart
plt.figure(figsize=(10, 6))
plt.plot(df['customer_id'], df['total_purchases'], marker='o', linestyle='-', color='b', label='Total Purchases')
plt.title('Total Purchases per Customer', fontsize=15)
plt.xlabel('Customer ID', fontsize=12)
plt.ylabel('Total Purchases', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plotting total value of purchases per customer as a line chart
plt.figure(figsize=(10, 6))
plt.plot(df['customer_id'], df['total_value'], marker='o', linestyle='-', color='r', label='Total Value (USD)')
plt.title('Total Value of Purchases per Customer', fontsize=15)
plt.xlabel('Customer ID', fontsize=12)
plt.ylabel('Total Value (USD)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
