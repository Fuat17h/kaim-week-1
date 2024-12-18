# Load and preprocess data

import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Load data from file_path

    Args:
        file_path (str): _file description_

    Returns:
        pd.DataFrame: _data description_
    """
    data = pd.read_csv(file_path)
    print("Column names in the dataset:", data.columns)  # Debugging
    # Normalize column names to lowercase
    data.columns = data.columns.str.strip().str.lower()
    
    # Ensure the 'date' column is present and parse it
    if "date" in data.columns:
        data["date"] = pd.to_datetime(data["date"], errors="coerce")
    else:
        raise KeyError("'date' column not found in the dataset.")
    
    return data