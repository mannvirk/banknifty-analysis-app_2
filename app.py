import streamlit as st
from core.zerodha import get_kite
from core.option_chain import get_banknifty_chain
from core.oi_signals import oi_bias
from core.papertrade import create_trade, update_trade

st.set_page_config("Bank Nifty Analyzer", layout="wide")
st.title("📊 Bank Nifty Analysis + Paper Trade")

kite = get_kite()
chain = get_banknifty_chain(kite)

bias, pcr = oi_bias(chain)

st.subheader("Option Chain")
st.dataframe(chain, use_container_width=True)

st.subheader("Market Bias")
st.metric("Bias", bias)
st.metric("PCR", pcr)

ltp = chain.iloc[len(chain)//2]["LTP_CE"]

if st.button("▶ Execute Paper Trade"):
    st.session_state.trade = create_trade(bias, ltp)

if "trade" in st.session_state:
    trade = update_trade(st.session_state.trade, ltp)
    st.write(trade)
