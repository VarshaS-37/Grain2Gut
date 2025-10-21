import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")


st.markdown("""
<style>
.stApp {
    background-image: url('https://img.freepik.com/premium-vector/paddy-rice-field-background_267448-280.jpg');  
    background-size: cover;
    background-attachment: fixed;
}
.block-container {
    padding-top: 2rem;
    padding-left: 6rem;
    padding-right: 6rem;
}
h2 {
    text-align: center !important;
}
.stColumns {
    gap: 60px !important;
}
.stButton>button {
    background-color:#FEF7A2;
    color:#2c3e50;
    font-size:20px;
    border-radius:10px;
    padding:10px 20px;
    border:none;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color:#D4E4C6;
}
</style>
""", unsafe_allow_html=True)


st.markdown(
    "<h2>16S rRNA Analysis of Millet-derived Lactic Acid Bacteria</h2>",
    unsafe_allow_html=True
)


if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()

def main():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Proso Millet PP355677"):
            go_to("page_1")
    with col2:
        if st.button("Foxtail Millet PP355678"):
            go_to("page_2")
    with col3:
        if st.button("Little Millet PP355679"):
            go_to("page_3")
    with col4:
        if st.button("Little Millet PP355680"):
            go_to("page_4")

def page_1():
    st.title("Proso Millet PP355677")
    st.write("This is content for Page 1.")
    if st.button("Back to Home"):
        go_to("home")

def page_2():
    st.title("Foxtail Millet PP355678")
    st.write("This is content for Page 2.")
    if st.button("Back to Home"):
        go_to("home")

def page_3():
    st.title("Little Millet PP355679")
    st.write("This is content for Page 3.")
    if st.button("Back to Home"):
        go_to("home")

def page_4():
    st.title("Little Millet PP355680")
    st.write("This is content for Page 4.")
    if st.button("Back to Home"):
        go_to("home")

if st.session_state.page == "home":
    main()
elif st.session_state.page == "page_1":
    page_1()
elif st.session_state.page == "page_2":
    page_2()
elif st.session_state.page == "page_3":
    page_3()
elif st.session_state.page == "page_4":
    page_4()
