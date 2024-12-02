import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# File to load
csv_file = 'csvs/MTA_Subway_Hourly_Ridership_2022.csv'

# Connect to the database
try:
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")
cur = conn.cursor()

# Load CSV into the table
with open(csv_file, 'r') as f:
    cur.copy_expert(
        """COPY subway_data(
            transit_timestamp, transit_mode, station_complex_id, station_complex, borough,
            payment_method, fare_class_category, ridership, transfers, latitude, longitude, georeference
        ) FROM STDIN WITH CSV HEADER""",
        f
    )

conn.commit()
cur.close()
conn.close()

print("Data successfully loaded into the database.")