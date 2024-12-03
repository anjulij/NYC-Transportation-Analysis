import pandas as pd
import os
import sys

def trim_csv_to_100(input_file, output_file):
    try:
        # Read the CSV file
        data = pd.read_csv(input_file)

        # Keep only the first 100 rows (if more exist)
        trimmed_data = data.head(100)

        # Save the trimmed data to a new CSV file
        trimmed_data.to_csv(output_file, index=False)
        print(f'Trimmed data saved to {output_file}')

        # Open the file in Excel (Windows only)
        if sys.platform == "win32":
            os.startfile(output_file)
        else:
            print(f'Opening in Excel is supported on Windows only.')
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


input_csv = 'csvs/mta_bus_hourly_ridership/MTA_Bus_Hourly_Ridership__Beginning_February_2022.csv'   
output_csv = 'trimmed_output.csv'

trim_csv_to_100(input_csv, output_csv)
