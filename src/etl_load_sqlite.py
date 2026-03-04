import sqlite3
import pandas as pd
import os

def load_csv_to_sqlite():
    # Ensure data/db directory exists
    os.makedirs('data/db', exist_ok=True)
    
    # Read CSV file
    df = pd.read_csv('data/raw/customers_raw.csv')
    
    # Create SQLite connection
    conn = sqlite3.connect('data/db/analytics.db')
    
    # Load data into table
    df.to_sql('customers_raw', conn, if_exists='replace', index=False)
    
    print(f"Loaded {len(df)} rows into customers_raw table")
    print("Sample data:")
    print(df.head())
    
    conn.close()

if __name__ == "__main__":
    load_csv_to_sqlite()
