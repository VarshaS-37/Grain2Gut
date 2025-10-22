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
    gap: 40px !important;
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


# ---------------------- Page Control ----------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to(page):
    st.session_state.page = page
    st.rerun()


# ---------------------- Home Page ----------------------
def home():
    st.markdown("<h2>Grain2Gut</h2>", unsafe_allow_html=True)
    st.markdown("<h2>Functional Prediction of Millet-derived Lactic Acid Bacteria</h2>", unsafe_allow_html=True)
    st.markdown("<h4>About App:</h4>", unsafe_allow_html=True)
    st.markdown("There are four millets which canbe selected n analyis of mille wise n overall analysis can also be done", unsafe_allow_html=True)
    st.write("")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("EC Analysis"):
            go_to("ec_analysis")
    with col2:
        if st.button("KO Analysis"):
            go_to("ko_analysis")
    with col3:
        if st.button("Pathway Analysis"):
            go_to("pwy_analysis")


# ---------------------- Millet Data Mapping ----------------------
millet_map = {
    "Proso Millet PP355677": "77",
    "Foxtail Millet PP355678": "78",
    "Little Millet PP355679": "79",
    "Little Millet PP355680": "80"
}


# ---------------------- EC Page ----------------------
# ---------------------- EC Page: Side-by-Side Layout ----------------------
def ec_page():
    st.title("EC Analysis")
    
    # Select Millet Strain at the top
    col1, col2, col3 = st.columns([3, 2, 3])
    with col2:
        st.markdown("<h4 style='text-align:center;'>Select Millet Strain</h4>", unsafe_allow_html=True)
        selected_strain = st.selectbox(
            "",
            list(millet_map.keys()),
            label_visibility="collapsed",
            key=f"strain_select_{st.session_state.page}",
        )
    suffix = millet_map[selected_strain]

    # Load dataframe if available
    try:
        df = pd.read_csv(f"picrust_output_files/ec{suffix}.csv")
    except FileNotFoundError:
        st.error(f"File ec{suffix}.csv not found.")
        return

    st.write("")  # spacing

    # ---------------------- Side-by-Side Columns ----------------------
    left_col, right_col = st.columns([2, 1])  # left bigger than right

    # ---- Left Column: Full DataFrame ----
    with left_col:
        st.markdown("<h4 style='text-align:center;'>EC DataFrame</h4>", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)

    # ---- Right Column: Textual Interpretation ----
    with right_col:
        st.markdown("<h4 style='text-align:center;'>Textual Interpretation</h4>", unsafe_allow_html=True)
        ec_ids = df['EC_ID'].unique().tolist() if 'EC_ID' in df.columns else []
        selected_ec = st.selectbox("Select EC ID", ec_ids, key="ec_select")
        
        if selected_ec:
            ec_summary = df[df['EC_ID'] == selected_ec]
            st.markdown(f"**Summary for EC ID {selected_ec}:**")
            st.dataframe(ec_summary, use_container_width=True)

    st.write("")  # spacing
    if st.button("Back to Home"):
        go_to("home")


# ---------------------- KO Page ----------------------
def ko_page():
    st.title("KO Analysis")
    col1, col2, col3 = st.columns([3, 2, 3])
    with col2:
        st.markdown("<h4 style='text-align:center;'>Select Millet Strain</h4>", unsafe_allow_html=True)
        selected = st.selectbox(
            "",
            list(millet_map.keys()),
            label_visibility="collapsed",
            key=f"select_{st.session_state.page}",
        )
    suffix = millet_map[selected]

    try:
        df = pd.read_csv(f"picrust_output_files/ko{suffix}.csv")
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.error(f"File ko{suffix}.csv not found.")

    if st.button("Back to Home"):
        go_to("home")


# ---------------------- Pathway Page ----------------------
def pwy_page():
    st.title("Pathway Analysis")
    col1, col2, col3 = st.columns([3, 2, 3])
    with col2:
        st.markdown("<h4 style='text-align:center;'>Select Millet Strain</h4>", unsafe_allow_html=True)
        selected = st.selectbox(
            "",
            list(millet_map.keys()),
            label_visibility="collapsed",
            key=f"select_{st.session_state.page}",
        )
    suffix = millet_map[selected]

    try:
        df = pd.read_csv(f"picrust_output_files/pwy_{suffix}.csv")
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.error(f"File pwy_{suffix}.csv not found.")

    if st.button("Back to Home"):
        go_to("home")


# ---------------------- Navigation ----------------------
page = st.session_state.page

if page == "home":
    home()
elif page == "ec_analysis":
    ec_page()
elif page == "ko_analysis":
    ko_page()
elif page == "pwy_analysis":
    pwy_page()
