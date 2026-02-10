from kiteconnect import KiteConnect
import streamlit as st

def get_kite():
    api_key = st.secrets["KITE_API_KEY"]
    access_token = st.secrets["KITE_ACCESS_TOKEN"]

    kite = KiteConnect(api_key=api_key)
    kite.set_access_token(access_token)
    return kite
