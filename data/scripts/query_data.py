import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def fetch_data_from_db(output_csv=None, desired_day=0, start_hour=0, end_hour=0):
    load_dotenv()
    
    # Database connection details
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    # Connect to PostgreSQL and fetch data
    try:
        engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

        # Define query
        query = """
            SELECT 
                transit_timestamp,
                latitude, 
                longitude, 
                ridership
            FROM 
                public.subway_data
            WHERE 
                EXTRACT(DOW FROM transit_timestamp) = %s AND
                EXTRACT(HOUR FROM transit_timestamp) BETWEEN %s AND %s;
        """
        # Fetch data
        data = pd.read_sql(query, con=engine, params=(desired_day, start_hour, end_hour))

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

# Fetch data and save it as a CSV
# fetch_data_from_db(output_csv="mta_subway_sample.csv")