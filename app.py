import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv('pwy_77.csv')
st.title("Millet derived Latic Acid Bacteria 16sRNA Analysis")

st.subheader("Pathways of millet PP355677")
st.dataframe(df)


