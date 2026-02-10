from kiteconnect import KiteConnect
import streamlit as st

def get_kite():
    api_key = st.secrets["oudhslhstgk67mc9rwvib781mbeaeerm"]
    access_token = st.secrets["RmerrnO3SlXjIQmaEQ5y22Su0rrJjET2"]

    kite = KiteConnect(api_key=api_key)
    kite.set_access_token(access_token)
    return kite

