import pandas as pd

def load_flight_data(file_path: str) -> pd.DataFrame:
    """
    Load flight CSV data.

    This function assumes a standardized CSV format used in electric aircraft
    flight logging systems.
    """
    df = pd.read_csv(file_path)
    return df
