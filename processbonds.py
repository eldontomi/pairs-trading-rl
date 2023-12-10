import pandas as pd

def prepare_bond_data(bra_csv_path, petbra_csv_path, output_bra_csv_path, output_petbra_csv_path):
    # Load the CSV files
    bra_df = pd.read_csv(bra_csv_path)
    petbra_df = pd.read_csv(petbra_csv_path)

    # Renaming the 'PX_LAST' column to 'close' and removing the 'YTD_CONV' column
    bra_df = bra_df.rename(columns={'PX_LAST': 'close'}).drop(columns=['YLD_CNV_LAST'])
    petbra_df = petbra_df.rename(columns={'PX_LAST': 'close'}).drop(columns=['YLD_CNV_LAST'])

    # Converting the 'Date' column to datetime for proper alignment and sorting
    bra_df['Date'] = pd.to_datetime(bra_df['Date'], dayfirst=True)
    petbra_df['Date'] = pd.to_datetime(petbra_df['Date'], dayfirst=True)

    # Sorting the data by date
    bra_df.sort_values('Date', inplace=True)
    petbra_df.sort_values('Date', inplace=True)

    # Aligning the dates and ensuring both datasets have the same dates for the first 252*4 rows
    min_common_date = max(bra_df['Date'].min(), petbra_df['Date'].min())
    max_common_date = min(bra_df['Date'].max(), petbra_df['Date'].max())

    # Filtering the dataframes to have the same date range
    filtered_bra_df = bra_df[(bra_df['Date'] >= min_common_date) & (bra_df['Date'] <= max_common_date)]
    filtered_petbra_df = petbra_df[(petbra_df['Date'] >= min_common_date) & (petbra_df['Date'] <= max_common_date)]

    # Ensuring that each dataframe has at least 252*4 rows
    required_rows = 252 * 4
    filtered_bra_df = filtered_bra_df.head(required_rows)
    filtered_petbra_df = filtered_petbra_df.head(required_rows)

    # Writing the prepared data to new CSV files
    filtered_bra_df.to_csv(output_bra_csv_path, index=False)
    filtered_petbra_df.to_csv(output_petbra_csv_path, index=False)

    print(f"Data saved to {output_bra_csv_path} and {output_petbra_csv_path}")

# Define the file paths for the original and output CSV files
bra_5_625_path = 'bra_5_625.csv'  # Replace with the actual file path
petbra_6_875_path = 'petbra_6_875.csv'  # Replace with the actual file path
output_bra_csv_path = 'output_bra_5_625.csv'  # Path for the output BRA CSV file
output_petbra_csv_path = 'output_petbra_6_875.csv'  # Path for the output PETBRA CSV file

# Preparing the data and writing to new CSV files
prepare_bond_data(bra_5_625_path, petbra_6_875_path, output_bra_csv_path, output_petbra_csv_path)
