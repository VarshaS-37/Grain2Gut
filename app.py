import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv('pwy_77.csv')
st.title("Millet derived Latic Acid Bacteria 16sRNA Analysis")

st.subheader("Pathways of millet PP355677")


st.markdown("""
    <style>
        .stApp {
            background-image: url('https://cdn.vectorstock.com/i/1000v/28/30/bacterial-background-thin-line-vector-24482830.jpg');  
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
          
        }
    </style>
""", unsafe_allow_html=True)


