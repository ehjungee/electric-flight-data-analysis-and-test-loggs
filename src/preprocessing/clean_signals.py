def clean_signals(df):
    """
    Basic signal cleaning:
    - Remove missing values
    - Clip abnormal sensor values

    This reflects real-world preprocessing of noisy flight sensor data.
    """
    df = df.copy()

    df = df.dropna()

    if "soc" in df.columns:
        df = df[(df["soc"] >= 0) & (df["soc"] <= 100)]

    return df
