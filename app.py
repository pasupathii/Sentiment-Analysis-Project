import streamlit as st
import pandas as pd

st.title("Sentiment Analysis App")

text = st.text_area("Enter Text")

if st.button("Analyze"):
    if "good" in text.lower():
        st.success("Positive Sentiment 😊")
    else:
        st.error("Negative Sentiment 😞")