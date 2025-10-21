import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv('pwy_77.csv')
st.title("Millet derived Latic Acid Bacteria 16sRNA Analysis")

st.subheader("Pathways of millet PP355677")


st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://drive.google.com/file/d/17a-B3xs-ReX-nKKZe9wazVuh-0FZ3Ssb/view?usp=sharing');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)


