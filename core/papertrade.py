from datetime import datetime
from config.settings import LOT_SIZE, SL_POINTS, TARGET_POINTS

def create_trade(signal, price):
    if signal not in ["Bullish", "Bearish"]:
        return None

    return {
        "Time": datetime.now().strftime("%H:%M"),
        "Signal": signal,
        "Entry": price,
        "SL": price - SL_POINTS,
        "Target": price + TARGET_POINTS,
        "Status": "OPEN",
        "PnL": 0
    }

def update_trade(trade, ltp):
    if trade["Status"] != "OPEN":
        return trade

    if ltp <= trade["SL"]:
        trade["Status"] = "SL HIT"
    elif ltp >= trade["Target"]:
        trade["Status"] = "TARGET HIT"

    trade["PnL"] = (ltp - trade["Entry"]) * LOT_SIZE
    return trade
