import pandas as pd
from datetime import datetime

def trim_csv_by_date(input_file, output_file, start_date, end_date, chunk_size=100000):
    # Convert the start and end dates to datetime objects
    start_date = datetime.strptime(start_date, '%m-%d-%y %H:%M')
    end_date = datetime.strptime(end_date, '%m-%d-%y %H:%M')

    # Open the output file in write mode and write the header only once
    with open(output_file, 'w') as f_out:
        header_written = False

        # Process the CSV in chunks
        for chunk in pd.read_csv(input_file, chunksize=chunk_size, low_memory=False):
            # Parse the 'transit_timestamp' column as datetime
            chunk['transit_timestamp'] = pd.to_datetime(
                chunk['transit_timestamp'], format='%m-%d-%y %I:%M', errors='coerce'
            )

            # Drop rows with invalid dates
            chunk = chunk.dropna(subset=['transit_timestamp'])

            # Filter the chunk for rows within the date range
            filtered_chunk = chunk[
                (chunk['transit_timestamp'] >= start_date) &
                (chunk['transit_timestamp'] <= end_date)
            ]

            # Write the filtered rows to the output file
            if not filtered_chunk.empty:
                filtered_chunk.to_csv(f_out, index=False, header=not header_written)
                header_written = True  # Ensure the header is written only once

    print(f'Trimmed CSV saved to {output_file}')

# Usage example:
input_file = 'csvs/MTA_Subway_Hourly_Ridership__Beginning_July_2020.csv'
output_file = 'trimmed_output.csv'
start_date = '01-01-22 00:00'  # Start date (inclusive)
end_date = '12-31-22 23:59'    # End date (inclusive)

trim_csv_by_date(input_file, output_file, start_date, end_date)