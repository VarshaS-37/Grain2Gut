import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv('pwy_77.csv')
st.title("Millet derived Latic Acid Bacteria 16sRNA Analysis")

st.subheader("Pathways of millet PP355677")
st.dataframe(df)

st.markdown("""
    <style>
        .stApp {
            background-image: url('https://media.istockphoto.com/id/1364601532/vector/illustration-of-a-field-of-millet-drawn-in-watercolor.jpg?s=612x612&w=0&k=20&c=p91DSTjLU401_esbPiGUG_2uR6_-1g9CQVnDjTTKP1I=');  
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            height: 100vh;
        }
    </style>
""", unsafe_allow_html=True)


