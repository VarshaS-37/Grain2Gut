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
    "Enterococcus casseliflavus (Proso Millet)": "77",
    "Weisella cibaria NM01 (Foxtail Millet)": "78",
    "Weisella cibaria NM01 (Little Millet)": "79",
    "Lactococcus lactis (Little Millet)": "80"
}
# ---------------------- EC Page: Dropdown Above Full DF ----------------------
def ec_page():
    st.markdown("<h4 style='text-align:center;'>EC Analysis</h4>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([3, 3, 3])
    with col2:
        st.markdown("<h4 style='text-align:center;'>Select the Millet LAB</h4>", unsafe_allow_html=True)
        selected_strain = st.selectbox(
            "",
            list(millet_map.keys()),
            label_visibility="collapsed",
            key=f"strain_select_{st.session_state.page}",
        )
    suffix = millet_map[selected_strain]

    # Load EC dataframe
    try:
        df = pd.read_csv(f"picrust_output_files/ec{suffix}.csv")
    except FileNotFoundError:
        st.error(f"File ec{suffix}.csv not found.")
        return

    # Load textual interpretation CSV
    try:
        text_df = pd.read_csv(f"picrust_output_files/ec{suffix}_text.csv")  # columns: ec_number, description
    except FileNotFoundError:
        st.error(f"Text file ec{suffix}_text.csv not found.")
        return

    st.write("")  # spacing

    # ---------------------- Side-by-Side Columns ----------------------
    left_col, right_col = st.columns([1, 2])  # left smaller, right bigger

    # ---- Left Column: EC number dropdown + Full EC DataFrame ----
    with left_col:
        st.markdown("<h4 style='text-align:center;'>Select a EC Number</h4>", unsafe_allow_html=True)
        if 'ec_number' in df.columns:
            selected_ec = st.selectbox("",df['ec_number'].unique(), key="ec_select")
        else:
            st.warning("Column 'ec_number' not found in dataframe.")
            selected_ec = None

        st.markdown("<h4 style='text-align:center;'>EC DataFrame</h4>", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)

    # ---- Right Column: Textual Interpretation ----
    with right_col:
        st.markdown("<h4 style='text-align:center;'>Interpretation</h4>", unsafe_allow_html=True)
        if selected_ec:
            ec_text = text_df[text_df['ec_number'] == selected_ec]
            if not ec_text.empty:
                st.markdown(f"**{selected_ec}**")
                st.markdown(ec_text.iloc[0]['description'])
            else:
                st.warning("No textual description found for this EC number.")

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
