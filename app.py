import streamlit as st
import requests
import pandas as pd

st.set_page_config(
   page_title="Polygon Score",
   page_icon="💯",
   menu_items={
      'About': "#### Check your Polygon Score Now",
      'Report a bug': "https://github.com/RutvikJ77",
    }
)
st.title("💯 Polygon Score")

wallet_address = st.text_input("Enter your wallet address:")

if st.button("Calculate"):
    if len(wallet_address)!=0:
        score = requests.post("https://analytics.polygon.technology/score/user-latest?address="+wallet_address).json()
        if len(score)!=0:
            st.write(score)
        else:
            st.warning("Please perform some transactions on Polygon.")
    else:
        st.warning("Enter your wallet address")
    