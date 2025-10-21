import streamlit as st
import pandas as pd
import plotly.express as px


st.markdown(
    """
    <h2 style='text-align: center; color: #2c3e50; white-space: nowrap; '>
        16srRNA Analysis of Millet derived Lactic Acid Bacteria 
    </h2>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
        .stApp {
            background-image: url('https://t3.ftcdn.net/jpg/01/94/82/02/360_F_194820208_QfSZW8rzs2E9Lq8dWouacJiK2Tzyz4iF.jpg');  
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            height: 100vh;
        }
    </style>
""", unsafe_allow_html=True)


def main():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Page 1"):
            page_1()

    with col2:
        if st.button("Page 2"):
            page_2()

    with col3:
        if st.button("Page 3"):
            page_3()

    with col4:
        if st.button("Page 4"):
            page_4()


def page_1():
    st.subheader("Page 1")
    st.write("This is content for Page 1.")

# Define content for Page 2
def page_2():
    st.subheader("Page 2")
    st.write("This is content for Page 2.")

# Define content for Page 3
def page_3():
    st.subheader("Page 3")
    st.write("This is content for Page 3.")

# Define content for Page 4
def page_4():
    st.subheader("Page 4")
    st.write("This is content for Page 4.")

if __name__ == "__main__":
    main()


