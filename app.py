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
        background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1pmfcg0I7dbMfe33dtp0DqbWexfMIZHaDgtQ_-ClkYu1KuvSPKpM6Jvn0tmdvuqicv48&usqp=CAU');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)


