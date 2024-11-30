import pandas as pd

# Load CSV
input_csv = 'csvs/MTA_Subway_Hourly_Ridership_2022.csv'  # Path to your original CSV
output_csv = 'csvs/mta_subway_hourly_ridership_2022_with_geom.csv'  # Path to save processed CSV

data = pd.read_csv(input_csv)

# Add WKT representation of geometry
data['georeference'] = data.apply(
    lambda row: f"SRID=4326;POINT({row['longitude']} {row['latitude']})",
    axis=1
)

# Save processed CSV
data.to_csv(output_csv, index=False)
print(f"Processed data saved to {output_csv}")