import pandas as pd

CSV_FILE_PATH = "data/pyth_merged_file.csv"

def filter_by_coordinates(lat_min, lat_max, lon_min, lon_max):
    try:
        data = pd.read_csv(CSV_FILE_PATH)
    except FileNotFoundError:
        print("The CSV data file was not found")
        return None
        
    if 'LAT' not in data.columns or 'LONG' not in data.columns:
        print("Dataset must contain 'LAT' and 'LONG' columns.")
        return None

    # Filter rows within the specified coordinate bounds
    filtered_data = data[
        (data['LAT'] >= lat_min) &
        (data['LAT'] <= lat_max) &
        (data['LONG'] >= lon_min) &
        (data['LONG'] <= lon_max)
    ]

    return filtered_data

filter_by_coordinates(145, 145.2, -40, -36) # example input
