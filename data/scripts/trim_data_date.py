import pandas as pd
from datetime import datetime

def trim_csv_by_date(input_file, output_file, start_date, end_date, chunk_size=100000):
    # Convert the start and end dates to datetime objects
    start_date = datetime.strptime(start_date, '%m-%d-%y %I:%M:%S %p')
    end_date = datetime.strptime(end_date, '%m-%d-%y %I:%M:%S %p')

     # Open the output file to ensure the header is written even if no rows are found
    with open(output_file, 'w') as f_out:
        header_written = False

        # Process the CSV in chunks
        for i, chunk in enumerate(pd.read_csv(input_file, chunksize=chunk_size, low_memory=False)):
            print(f"Processing chunk {i+1}...")

            # Apply the custom timestamp parser
            chunk['transit_timestamp'] = pd.to_datetime(chunk['transit_timestamp'], errors='coerce')

            # Report how many valid timestamps were parsed
            valid_timestamps = chunk['transit_timestamp'].notna().sum()
            print(f"Valid timestamps in chunk {i+1}: {valid_timestamps}")

            # Write the header even if no valid rows found in the first chunk
            if not header_written:
                chunk.head(0).to_csv(f_out, index=False)
                header_written = True

            # Drop rows with invalid dates
            chunk = chunk.dropna(subset=['transit_timestamp'])

            # Print some valid rows for verification
            if not chunk.empty:
                print(chunk.head())  

            # Filter the chunk for rows within the date range
            filtered_chunk = chunk[
                (chunk['transit_timestamp'] >= start_date) &
                (chunk['transit_timestamp'] <= end_date)
            ]

            print(f"Filtered rows in chunk {i+1}: {len(filtered_chunk)}")

            # Write the filtered rows to the output file
            if not filtered_chunk.empty:
                filtered_chunk.to_csv(f_out, index=False, header=False)

    print(f'Trimmed CSV saved to {output_file}')

# Define variables
input_file = 'csvs/MTA_Subway_Hourly_Ridership__Beginning_July_2020.csv'
output_file = 'MTA_Subway_Hourly_Ridership__Beginning_July_2020_trimmed.csv'
start_date = '01-01-22 12:00:00 AM'
end_date = '12-31-22 11:59:00 PM'

trim_csv_by_date(input_file, output_file, start_date, end_date)