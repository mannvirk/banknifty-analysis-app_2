import pandas as pd

def get_banknifty_chain(kite):
    inst = pd.DataFrame(kite.instruments("NFO"))
    df = inst[(inst["name"] == "BANKNIFTY") & (inst["segment"] == "NFO-OPT")]

    df["expiry"] = pd.to_datetime(df["expiry"])
    expiry = df["expiry"].min()
    df = df[df["expiry"] == expiry]

    tokens = ["NFO:" + t for t in df["tradingsymbol"]]
    quotes = kite.quote(tokens)

    rows = []
    for _, r in df.iterrows():
        q = quotes["NFO:" + r["tradingsymbol"]]
        rows.append({
            "Strike": r["strike"],
            "Type": r["instrument_type"],
            "LTP": q["last_price"],
            "OI": q["oi"],
            "Volume": q["volume"]
        })

    oc = pd.DataFrame(rows)
    ce = oc[oc["Type"] == "CE"].set_index("Strike")
    pe = oc[oc["Type"] == "PE"].set_index("Strike")

    chain = ce.join(pe, lsuffix="_CE", rsuffix="_PE").reset_index()
    return chain.sort_values("Strike")
