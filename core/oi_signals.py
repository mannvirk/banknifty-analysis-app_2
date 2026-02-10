def oi_bias(chain):
    pcr = chain["OI_PE"].sum() / chain["OI_CE"].sum()

    if pcr > 1.1:
        return "Bullish", round(pcr, 2)
    elif pcr < 0.9:
        return "Bearish", round(pcr, 2)
    else:
        return "Neutral", round(pcr, 2)
