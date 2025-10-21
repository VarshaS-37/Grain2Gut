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
            background-image: url('https://img.freepik.com/premium-vector/paddy-rice-field-background_267448-280.jpg');  
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            height: 100vh;
        }
    </style>
""", unsafe_allow_html=True)
def inject_custom_css():
    
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #f7d8e2;  /* Button background */
            color:  #2c3e50;  /* Text color */
            font-size: 18px;  /* Font size */
            border-radius: 10px;  /* Round corners */
            padding: 10px 20px;  /* Padding around text */
            border: none;
            transition: background-color 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: #45a049;  /* Button hover background */
        }

        /* Add space between buttons */
        .stColumns>div {
            padding: 0 30px;  /* Horizontal space between buttons */
        }

        </style>
    """, unsafe_allow_html=True)

def main():
    col1, col2, col3, col4 = st.columns(4)
    inject_custom_css()
    with col1:
        if st.button("Proso Millet PP355677"):
            page_1()

    with col2:
        if st.button("Foxtail Millet PP355678"):
            page_2()

    with col3:
        if st.button("Little Millet PP355679"):
            page_3()

    with col4:
        if st.button("Little Millet PP355680"):
            page_4()


def page_1():
    st.subheader("Page 1")
    st.write("This is content for Page 1.")


def page_2():
    st.subheader("Page 2")
    st.write("This is content for Page 2.")


def page_3():
    st.subheader("Page 3")
    st.write("This is content for Page 3.")


def page_4():
    st.subheader("Page 4")
    st.write("This is content for Page 4.")

if __name__ == "__main__":
    main()


