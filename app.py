import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ---------------------- CSS ----------------------
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
h2, h1 {
    text-align: center !important;
    color: #2c3e50;
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
    background-color:#DFFBB9;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to(page):
    st.session_state.page = page
    st.rerun()

def home():
    st.markdown("<h2>16S rRNA Analysis of Millet-derived Lactic Acid Bacteria</h2>", unsafe_allow_html=True)
    st.write("")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Proso Millet PP355677"):
            go_to("millet1")
    with col2:
        if st.button("Foxtail Millet PP355678"):
            go_to("millet2")
    with col3:
        if st.button("Little Millet PP355679"):
            go_to("millet3")
    with col4:
        if st.button("Little Millet PP355680"):
            go_to("millet4")

tag_to_suffix = {
    "millet1": "77",
    "millet2": "78",
    "millet3": "79",
    "millet4": "80",
}


def millet_page(title, tag):
    st.title(title)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("EC Analysis"):
            go_to(f"{tag}_ec")
    with col2:
        if st.button("KO Analysis"):
            go_to(f"{tag}_ko")
    with col3:
        if st.button("Pathway Analysis"):
            go_to(f"{tag}_pwy")
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Back to Home"):
        go_to("home")


def ec_page(title, tag):
    st.title(f"{title} - EC Analysis")
    suffix = tag_to_suffix.get(tag, "")
    try:
        df = pd.read_csv(f"ec{suffix}.csv")
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.error(f"File ec{suffix}.csv not found.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back to Millet Page"):
            go_to(tag)
    with col2:
        if st.button("Back to Home"):
            go_to("home")

def ko_page(title, tag):
    st.title(f"{title} - KO Analysis")
    suffix = tag_to_suffix.get(tag, "")
    try:
        df = pd.read_csv(f"ko{suffix}.csv")
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.error(f"File ko{suffix}.csv not found.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back to Millet Page"):
            go_to(tag)
    with col2:
        if st.button("Back to Home"):
            go_to("home")

def pwy_page(title, tag):
    st.title(f"{title} - Pathway Analysis")
    suffix = tag_to_suffix.get(tag, "")
    try:
        df = pd.read_csv(f"pwy_{suffix}.csv")
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.error(f"File pwy_{suffix}.csv not found.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back to Millet Page"):
            go_to(tag)
    with col2:
        if st.button("Back to Home"):
            go_to("home")


page = st.session_state.page

if page == "home":
    home()

elif page == "millet1":
    millet_page("Proso Millet PP355677", "millet1")
elif page == "millet2":
    millet_page("Foxtail Millet PP355678", "millet2")
elif page == "millet3":
    millet_page("Little Millet PP355679", "millet3")
elif page == "millet4":
    millet_page("Little Millet PP355680", "millet4")

elif page == "millet1_ec":
    ec_page("Proso Millet PP355677", "millet1")
elif page == "millet2_ec":
    ec_page("Foxtail Millet PP355678", "millet2")
elif page == "millet3_ec":
    ec_page("Little Millet PP355679", "millet3")
elif page == "millet4_ec":
    ec_page("Little Millet PP355680", "millet4")

elif page == "millet1_ko":
    ko_page("Proso Millet PP355677", "millet1")
elif page == "millet2_ko":
    ko_page("Foxtail Millet PP355678", "millet2")
elif page == "millet3_ko":
    ko_page("Little Millet PP355679", "millet3")
elif page == "millet4_ko":
    ko_page("Little Millet PP355680", "millet4")

elif page == "millet1_pwy":
    pwy_page("Proso Millet PP355677", "millet1")
elif page == "millet2_pwy":
    pwy_page("Foxtail Millet PP355678", "millet2")
elif page == "millet3_pwy":
    pwy_page("Little Millet PP355679", "millet3")
elif page == "millet4_pwy":
    pwy_page("Little Millet PP355680", "millet4")

