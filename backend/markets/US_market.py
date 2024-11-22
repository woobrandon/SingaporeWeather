import pandas as pd

def get_us_ticker_symbols():
    try:
        return pd.read_csv("./Backend/markets/nasdaq_screener.csv")
    except:
        raise Exception(f"Failed to fetch ticker symbols")