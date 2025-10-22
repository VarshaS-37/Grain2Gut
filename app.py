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
    st.markdown("<h2 style='text-align:center;'>Grain2Gut</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Functional Prediction of Millet-derived Lactic Acid Bacteria</h3>", unsafe_allow_html=True)

    # ---------------------- Sidebar with Project Description ----------------------
    with st.sidebar.expander("About This Project", expanded=True):
        st.markdown("""
        **Grain2Gut** is an interactive app for analyzing millet-derived lactic acid bacteria (LAB).  
        Features include:  
        - Functional prediction using PICRUSt.  
        - Exploration of EC numbers, KO identifiers, and metabolic pathways.  
        - Textual interpretation for each feature.  

        Use the **Detailed Analysis** box on the main page to access EC, KO, and Pathway analyses.  
        """)
    
    st.write("")  # spacing

    # ---------------------- Main Page Layout ----------------------
    # Two columns: left for spacing or future boxes, right for Detailed Analysis box
    left_col, right_col = st.columns([1, 2])

    # ---- Right Column: Detailed Analysis Box ----
    with right_col:
        st.markdown(
            """
            <div style="
                background-color: #FEF7A2;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            ">
                <h4 style='text-align:center;'>Detailed Analysis</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Buttons inside Detailed Analysis box
        st.write("")  # spacing
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
    
    st.markdown("<h3 style='text-align:center;'>EC Analysis</h3>", unsafe_allow_html=True)
     # ---------------------- Sidebar with instructions ----------------------
    with st.sidebar.expander("How to Use this Page", expanded=True):
        st.markdown("""
        **Instructions:**
        1. Select the millet LAB from the dropdown at the top.
        2. On the left, the entire EC dataframe for the selected LAB is displayed.
        3. Use the **EC number dropdown** above the dataframe to select an EC number.
        4. The right column will show the textual interpretation for the selected EC number.
        5. Use the "Back to Home" button at the bottom to return to the home page.
        """)
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


# ---------------------- KO Page: Side-by-Side + Sidebar ----------------------
def ko_page():
    
    st.markdown("<h3 style='text-align:center;'>KO Analysis</h3>", unsafe_allow_html=True)
    
    # ---------------------- Sidebar with instructions ----------------------
    with st.sidebar.expander("How to Use this Page", expanded=True):
        st.markdown("""
        **Instructions:**
        1. Select the millet LAB from the dropdown at the top.
        2. On the left, the entire KO dataframe for the selected LAB is displayed.
        3. Use the **KO ID dropdown** above the dataframe to select a KO ID.
        4. The right column will show the textual interpretation for the selected KO number.
        5. Use the "Back to Home" button at the bottom to return to the home page.
        """)
    
    # ---------------------- Millet LAB Selection ----------------------
    col1, col2, col3 = st.columns([3, 3, 3])
    with col2:
        st.markdown("<h4 style='text-align:center;'>Select the Millet LAB</h4>", unsafe_allow_html=True)
        selected_strain = st.selectbox(
            "",
            list(millet_map.keys()),
            label_visibility="collapsed",
            key=f"ko_strain_select_{st.session_state.page}",
        )
    suffix = millet_map[selected_strain]

    # ---------------------- Load KO DataFrame ----------------------
    try:
        df = pd.read_csv(f"picrust_output_files/ko{suffix}.csv")
    except FileNotFoundError:
        st.error(f"File ko{suffix}.csv not found.")
        return

    # Load textual interpretation CSV
    try:
        text_df = pd.read_csv(f"picrust_output_files/ko{suffix}_text.csv")  # columns: ko_number, description
    except FileNotFoundError:
        st.error(f"Text file ko{suffix}_text.csv not found.")
        return

    st.write("")  # spacing

    # ---------------------- Side-by-Side Columns ----------------------
    left_col, right_col = st.columns([1, 2])  # left smaller, right bigger

    # ---- Left Column: KO number dropdown + Full KO DataFrame ----
    with left_col:
        st.markdown("<h4 style='text-align:center;'>Select a KO ID</h4>", unsafe_allow_html=True)
        if 'ko_id' in df.columns:
            selected_ko = st.selectbox("", df['ko_id'].unique(), key="ko_select")
        else:
            st.warning("Column 'ko_number' not found in dataframe.")
            selected_ko = None

        st.markdown("<h4 style='text-align:center;'>KO DataFrame</h4>", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)

    # ---- Right Column: Textual Interpretation ----
    with right_col:
        st.markdown("<h4 style='text-align:center;'>Interpretation</h4>", unsafe_allow_html=True)
        if selected_ko:
            ko_text = text_df[text_df['ko_id'] == selected_ko]
            if not ko_text.empty:
                st.markdown(f"**{selected_ko}**")
                st.markdown(ko_text.iloc[0]['description'])
            else:
                st.warning("No textual description found for this KO number.")

    st.write("")  # spacing
    if st.button("Back to Home"):
        go_to("home")



# ---------------------- Pathway Page: Side-by-Side + Sidebar ----------------------
def pwy_page():
    
    st.markdown("<h3 style='text-align:center;'>Pathway Analysis</h3>", unsafe_allow_html=True)
    
    # ---------------------- Sidebar with instructions ----------------------
    with st.sidebar.expander("How to Use this Page", expanded=True):
        st.markdown("""
        **Instructions:**
        1. Select the millet LAB from the dropdown at the top.
        2. On the left, the entire pathway dataframe for the selected LAB is displayed.
        3. Use the **Pathway ID dropdown** above the dataframe to select a pathway.
        4. The right column will show the textual interpretation for the selected pathway.
        5. Use the "Back to Home" button at the bottom to return to the home page.
        """)
    
    # ---------------------- Millet LAB Selection ----------------------
    col1, col2, col3 = st.columns([3, 3, 3])
    with col2:
        st.markdown("<h4 style='text-align:center;'>Select the Millet LAB</h4>", unsafe_allow_html=True)
        selected_strain = st.selectbox(
            "",
            list(millet_map.keys()),
            label_visibility="collapsed",
            key=f"pwy_strain_select_{st.session_state.page}",
        )
    suffix = millet_map[selected_strain]

    # ---------------------- Load Pathway DataFrame ----------------------
    try:
        df = pd.read_csv(f"picrust_output_files/pwy_{suffix}.csv")
    except FileNotFoundError:
        st.error(f"File pwy_{suffix}.csv not found.")
        return

    # Load textual interpretation CSV
    try:
        text_df = pd.read_csv(f"picrust_output_files/pwy{suffix}_text.csv")  # columns: pathway_id, description
    except FileNotFoundError:
        st.error(f"Text file pwy{suffix}_text.csv not found.")
        return

    st.write("")  # spacing

    # ---------------------- Side-by-Side Columns ----------------------
    left_col, right_col = st.columns([1, 2])  # left smaller, right bigger

    # ---- Left Column: Pathway ID dropdown + Full Pathway DataFrame ----
    with left_col:
        st.markdown("<h4 style='text-align:center;'>Select a Pathway</h4>", unsafe_allow_html=True)
        if 'Pathway' in df.columns:
            selected_pwy = st.selectbox("", df['Pathway'].unique(), key="pwy_select")
        else:
            st.warning("Column 'pathway_id' not found in dataframe.")
            selected_pwy = None

        st.markdown("<h4 style='text-align:center;'>Pathway DataFrame</h4>", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)

    # ---- Right Column: Textual Interpretation ----
    with right_col:
        st.markdown("<h4 style='text-align:center;'>Interpretation</h4>", unsafe_allow_html=True)
        if selected_pwy:
            pwy_text = text_df[text_df['Pathway'] == selected_pwy]
            if not pwy_text.empty:
                st.markdown(f"**{selected_pwy}**")
                st.markdown(pwy_text.iloc[0]['description'])
            else:
                st.warning("No textual description found for this pathway.")

    st.write("")  # spacing
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
