 # Functions for descriptive statistics
 
import pandas as pd

def calculate_headline_stats(df, column="headline"):
    """Calculate basic statistics for headline lengths.
    
    Args:
        df (pd.DataFrame): The input data.
        column (str): The column containing headlines. Defaults to "headline".

    Returns:
        pd.Series: A series of headline length statistics.
    """
    df["headline_length"] = df[column].str.len()
    stats = df["headline_length"].describe()
    return stats

def count_articles_per_publisher(df, column="publisher"):
    """Count the number of articles per publisher.
    
    Args:
        df (pd.DataFrame): The input data.
        column (str): The column containing publisher names. Defaults to "publisher".
    Returns:
        pd.Series: A series of counts of articles per publisher.
    """
    return df[column].value_counts()

def analyze_publication_trends(df: pd.DataFrame, column: str = "date"):
    """Analyze publication trends over time.
    
    Args:
        df (pd.DataFrame): The input data.
        column (str): The column containing publication dates.
    Returns:
        pd.Series: A time series of publication counts.
    """
    if column not in df.columns:
        raise KeyError(f"'{column}' column not found in the dataset.")
    
    # Check the date column is in datetime format
    df[column] = pd.to_datetime(df[column], errors="coerce")
    
    # Drop rows with invalid dates
    df = df.dropna(subset=[column])
    
    # Set the date as the index for time series analysis
    df.set_index(column, inplace=True)
    
    # Resample to daily frequency and count the number of publications
    publication_trends = df.resample("D").size()
    
    return publication_trends