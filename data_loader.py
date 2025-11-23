import pandas as pd

def load_data(file_path):
    """
    Loads the FMCG sales data from a CSV file.
    
    Args:
        file_path (str): The path to the CSV file.
        
    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred during data loading: {e}")
        return None

def initial_data_check(df):
    """
    Performs initial checks on the loaded DataFrame.
    """
    if df is not None:
        print("\n--- Initial Data Check ---")
        print("\nFirst 5 rows:")
        print(df.head())
        print("\nColumn information:")
        print(df.info())
        print("\nMissing values:")
        print(df.isnull().sum())
        print("\nUnique values in key categorical columns:")
        for col in ['brand', 'segment', 'category', 'channel', 'region', 'pack_type']:
            if col in df.columns:
                print(f"- {col}: {df[col].nunique()} unique values")

if __name__ == '__main__':
    # Define the path to the downloaded data file
    data_file_path = 'data/FMCG_2022_2024.csv'
    
    # Load the data
    df = load_data(data_file_path)
    
    # Perform initial checks
    initial_data_check(df)
