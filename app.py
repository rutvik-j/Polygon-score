import streamlit as st
import requests
import pandas as pd
from ethereum.utils import check_checksum

st.set_page_config(
   page_title="Polygon Score",
   page_icon="💯",
   menu_items={
      'About': "#### Check your Polygon Score Now",
      'Report a bug': "https://github.com/RutvikJ77",
    }
)
st.title("💯 Polygon Score")

col1, col2 = st.columns((3,1))

wallet_address = col1.text_input("Enter your wallet address:")
check_address = False

with col2.expander("Confused?"):
    st.markdown("Please check the [docs](https://analytics.polygon.technology/score/docs) users score and element section for more info.")


if col1.button("Calculate"):

    if len(wallet_address) == 0:
        st.warning("Please enter your wallet address")
    else:
        try:
            check_address = check_checksum(wallet_address)
        except:
            st.warning("Please enter a valid wallet Address")

    if check_address:
        score = requests.post("https://analytics.polygon.technology/score/user-latest?address="+wallet_address).json()
        if len(score)!=0:
            score_100 = score[0]["Score100"]
            if score_100 > 50:
                st.success( f"🚀 Congratulations! Your score is {score_100}. You can particpate for the [DeFi contest](https://forms.gle/Eb9RogYa4NetDom89)")
                st.write(score)
                st.markdown("![Congratulations](https://media.giphy.com/media/l49JHLpRSLhecYEmI/giphy.gif)")
            else:
                st.warning(f"Your score is {score_100}")
                st.write(score)
        else:
            st.warning("Please perform some transactions on Polygon.")

st.info("Note - A minimum score of 50 is required to be eligible to participate in the contest.")

