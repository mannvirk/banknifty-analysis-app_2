import pandas as pd

def indicators(df):
    delta = df["close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    rs = gain.rolling(14).mean() / loss.rolling(14).mean()
    df["RSI"] = 100 - (100 / (1 + rs))

    df["EMA_200"] = df["close"].ewm(span=200).mean()

    tp = (df["high"] + df["low"] + df["close"]) / 3
    df["VWAP"] = (tp * df["volume"]).cumsum() / df["volume"].cumsum()

    return df
