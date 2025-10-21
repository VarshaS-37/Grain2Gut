import streamlit as st
import pandas as pd
import os

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

# ---------------------- NAVIGATION ----------------------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "selected_id" not in st.session_state:
    st.session_state.selected_id = None

def go_to(page, selected_id=None):
    st.session_state.page = page
    st.session_state.selected_id = selected_id
    st.rerun()

# ---------------------- HOME PAGE ----------------------
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

# ---------------------- MILLET PAGE ----------------------
def millet_page(title, tag):
    st.title(title)
    st.write("Select which type of analysis you want to explore:")

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
    if st.button("⬅ Back to Home"):
        go_to("home")

# ---------------------- EC, KO, PWY TABLE FUNCTIONS ----------------------
def show_table(csv_file, tag, analysis_type):
    if not os.path.exists(csv_file):
        st.error(f"{csv_file} not found.")
        return
    df = pd.read_csv(csv_file)
    st.write(f"### {analysis_type.upper()} Table")
    st.write("Click on an ID to view details:")

    for _, row in df.iterrows():
        id_col = f"{analysis_type}_id" if f"{analysis_type}_id" in df.columns else df.columns[0]
        func = row.get("function", "")
        item_id = str(row[id_col])
        if st.button(f"{item_id} — {func}", key=f"{item_id}_{analysis_type}"):
            go_to(f"{tag}_{analysis_type}_detail", selected_id=item_id)

# ---------------------- DETAIL PAGE FUNCTION ----------------------
def show_detail_page(title, tag, analysis_type):
    item_id = st.session_state.selected_id
    st.title(f"{title} - {analysis_type.upper()} Detail")

    if not item_id:
        st.warning(f"No {analysis_type.upper()} ID selected.")
        return

    st.subheader(f"Details for {item_id}")
    file_name = f"{item_id}.txt"  # expects file in same folder
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            desc = f.read()
        st.write(desc)
    else:
        st.info(f"No detailed description available for {item_id} yet.")

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"⬅ Back to {analysis_type.upper()} Table"):
            go_to(f"{tag}_{analysis_type}")
    with col2:
        if st.button("🏠 Back to Home"):
            go_to("home")

# ---------------------- EC/KO/PWY PAGE WRAPPERS ----------------------
def ec_page(title, tag):
    st.title(f"{title} - EC Analysis")
    show_table(f"{tag}_ec.csv", tag, "ec")

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back to Millet Page"):
            go_to(tag)
    with col2:
        if st.button("🏠 Back to Home"):
            go_to("home")

def ko_page(title, tag):
    st.title(f"{title} - KO Analysis")
    show_table(f"{tag}_ko.csv", tag, "ko")

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back to Millet Page"):
            go_to(tag)
    with col2:
        if st.button("🏠 Back to Home"):
            go_to("home")

def pwy_page(title, tag):
    st.title(f"{title} - Pathway Analysis")
    show_table(f"{tag}_pwy.csv", tag, "pwy")

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ Back to Millet Page"):
            go_to(tag)
    with col2:
        if st.button("🏠 Back to Home"):
            go_to("home")

# ---------------------- ROUTING ----------------------
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

# detail pages for EC / KO / Pathway
elif page == "millet1_ec_detail":
    show_detail_page("Proso Millet PP355677", "millet1", "ec")
elif page == "millet2_ec_detail":
    show_detail_page("Foxtail Millet PP355678", "millet2", "ec")
elif page == "millet3_ec_detail":
    show_detail_page("Little Millet PP355679", "millet3", "ec")
elif page == "millet4_ec_detail":
    show_detail_page("Little Millet PP355680", "millet4", "ec")

elif page == "millet1_ko_detail":
    show_detail_page("Proso Millet PP355677", "millet1", "ko")
elif page == "millet2_ko_detail":
    show_detail_page("Foxtail Millet PP355678", "millet2", "ko")
elif page == "millet3_ko_detail":
    show_detail_page("Little Millet PP355679", "millet3", "ko")
elif page == "millet4_ko_detail":
    show_detail_page("Little Millet PP355680", "millet4", "ko")

elif page == "millet1_pwy_detail":
    show_detail_page("Proso Millet PP355677", "millet1", "pwy")
elif page == "millet2_pwy_detail":
    show_detail_page("Foxtail Millet PP355678", "millet2", "pwy")
elif page == "millet3_pwy_detail":
    show_detail_page("Little Millet PP355679", "millet3", "pwy")
elif page == "millet4_pwy_detail":
    show_detail_page("Little Millet PP355680", "millet4", "pwy")

