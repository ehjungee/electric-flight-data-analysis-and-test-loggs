import numpy as np

def convert_units(df):
    """
    Convert raw units to analysis-ready units.
    - altitude: m -> ft
    - wind speed: m/s -> kt (if needed)
    """
    df = df.copy()

    if "altitude_m" in df.columns:
        df["altitude_ft"] = df["altitude_m"] * 3.28084

    if "wind_speed" in df.columns:
        df["wind_speed_kt"] = df["wind_speed"] * 1.94384

    return df


def decompose_wind(df):
    """
    Decompose wind vector into longitudinal, lateral, and vertical components.
    Assumes wind angles are provided or approximated.
    """
    df = df.copy()

    # Placeholder angles (in real case, derived from heading & METAR)
    if "wind_speed_kt" in df.columns:
        df["wind_longitudinal"] = df["wind_speed_kt"] * np.random.uniform(-1, 1, len(df))
        df["wind_lateral"] = df["wind_speed_kt"] * np.random.uniform(-0.5, 0.5, len(df))
        df["wind_vertical"] = df["wind_speed_kt"] * np.random.uniform(-0.1, 0.1, len(df))

    return df
