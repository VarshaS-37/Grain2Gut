import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv('pwy_77.csv')
st.title("Millet derived Latic Acid Bacteria 16sRNA Analysis")

st.subheader("Pathways of millet PP355677")


st.markdown("""
    <style>
        .stApp {
            background-image: url('https://media.istockphoto.com/id/541113276/vector/seamless-vector-pattern-of-germs-and-bacteria.jpg?s=612x612&w=0&k=20&c=M_kNtcWdpMHXNtOe6kxE32NnE3wDvxD7-Jma3ZNXaEs=');  /* Local file path */
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            height: 100vh;  /* Full height background */
        }
    </style>
""", unsafe_allow_html=True)


