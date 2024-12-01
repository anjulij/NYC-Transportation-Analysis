import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

def fetch_data_from_db(output_csv=None):
    load_dotenv()
    
    # Database connection details
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    # Connect to PostgreSQL and fetch data
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("Connection successful!")
 
        query = """
            SELECT 
                transit_timestamp,
                latitude, 
                longitude, 
                ridership
            FROM 
                subway_data;
        """
        data = pd.read_sql(query, conn)

        # Save to CSV
        if output_csv:
            data.to_csv(output_csv, index=False)
            print(f"Data saved to {output_csv}")

        return data
    
    except psycopg2.OperationalError as e:
        print(f"Error: Unable to connect to the database. {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    finally:
        if 'conn' in locals() and conn is not None:
            conn.close()
            print("Database connection closed.")

# Fetch data and save it as a CSV
fetch_data_from_db(output_csv="mta_subway_sample.csv")