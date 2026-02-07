def analyze_wind_impact(df):
    """
    Analyze correlation between wind variables and performance metrics.

    This module reflects findings that wind is a dominant factor
    in electric aircraft performance variation.
    """
    wind_cols = ["wind_speed", "wind_direction"]
    target = "soc"

    return df[wind_cols + [target]].corr()
