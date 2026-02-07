import matplotlib.pyplot as plt

def plot_time_series(df, x_col, y_col, title):
    """
    Plot time-series flight data for quick inspection.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(df[x_col], df[y_col])
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.show()
