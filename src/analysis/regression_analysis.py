import statsmodels.api as sm

def run_regression(df, target_col, feature_cols):
    """
    Run linear regression to identify key factors affecting flight performance.

    Example:
    target_col = "soc_change_rate"
    feature_cols = ["wind_speed", "airspeed_mps", "altitude_m"]
    """
    X = df[feature_cols]
    X = sm.add_constant(X)
    y = df[target_col]

    model = sm.OLS(y, X).fit()
    return model
