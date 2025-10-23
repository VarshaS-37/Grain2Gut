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

def footer():
    st.markdown("""
    <style>
    .footer-container {
        position: fixed;
        left: 50%;
        bottom: 10px;  /* distance from bottom */
        transform: translateX(-50%);
        background-color: #ffff66;  /* Yellow box */
        color: black;
        padding: 10px 20px;
        font-size: 14px;
        border-radius: 8px;  /* rounded corners */
        z-index: 100;
        text-align: center;
    }
    .footer-container a {
        color: 	 #004d66;  /* Dark blue links */
        text-decoration: none;
        font-weight: bold;
    }
    .footer-container a:hover {
        text-decoration: underline;
    }
    </style>

    <div class="footer-container">
        Jointly created by 
        <a href="https://github.com/VarshaS-37" target="_blank">Varsha</a> &
        <a href="https://github.com/Sandhyae2" target="_blank">Sandhya</a> |
        <a href="https://github.com/VarshaS-37/Grain2Gut/tree/main" target="_blank">GitHub Repo</a>
    </div>
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
    st.markdown("<h3 style='text-align:center;'>Linking genomic potential of Millet derived Lactic Acid Bacteria to food and probiotic applications</h3>", unsafe_allow_html=True)
    st.write("") 
    # ---------------------- Sidebar with Project Description ----------------------
    with st.sidebar.expander("About This App", expanded=False):
        st.markdown("""
        1. This app is based on a research paper by our guide, where lactic acid bacteria (LAB) were isolated and characterized from millets([research paper link](https://github.com/VarshaS-37/Grain2Gut/blob/main/Isolation_%26_characterization_of_biological_traits_of_millet-derived_lactic_acid_bacteria.pdf)).
        2. Among the isolates, four LAB strains showed probiotic characteristics, and their 16S rRNA partial sequences were submitted to NCBI.
        3. These sequences have been used for functional prediction using PICRUSt (Phylogenetic Investigation of Communities by Reconstruction of Unobserved States).
        4. The raw PICRUSt outputs were processed to obtain KO (KEGG Orthology), EC (Enzyme Commission), and PWY (Pathway) dataframes.
        5. Each dataframe was independently linked to reference information from databases.
        6. These dataframes are present in the **Meta Data** section and are used for further analysis.
        """)


   
    # ---------------------- Main Page Layout ----------------------
    left_col, middle_col, right_col = st.columns([1, 1, 1])  # left & middle for extra buttons/spaces, right for Detailed Analysis
    
    # ---- Left Column: additional buttons ----
    with left_col:
        if st.button("Summarized Analysis"):
            go_to("summarized_analysis")
        
    
    # ---- Middle Column: additional buttons ----
    with middle_col:
        if st.button("Millet-wise Analysis"):
            go_to("milletwise_analysis")
        
    
    with right_col:
        # Detailed Analysis heading
        st.markdown("<h4 style='text-align:center; margin-bottom:20px;'>Meta Data</h4>", unsafe_allow_html=True)
       
    
        # Center buttons below the heading
        for label, page_key in [("EC Analysis", "ec_analysis"), ("KO Analysis", "ko_analysis"), ("Pathway Analysis", "pwy_analysis")]:
            col1, col2, col3 = st.columns([1, 2, 1])  # middle column holds the button
            with col2:
                if st.button(label, key=label):
                    go_to(page_key)
    footer()
     

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
    with st.sidebar.expander("How to Use this Page", expanded=False):
        st.markdown("""
        **Instructions:**
        1. Select the millet LAB from the dropdown at the top.
        2. On the left, the entire EC dataframe for the selected LAB is displayed.
        3. Use the **EC number dropdown** above the dataframe to select an EC number.
        4. The right column will show the textual interpretation for the selected EC number.
        5. Use the "Back to Home" button at the bottom to return to the home page.
        """)
    with st.sidebar.expander("What is an EC Number?", expanded=False):
        st.markdown("""
        **EC (Enzyme Commission) numbers** are a numerical classification scheme for enzymes, 
        based on the chemical reactions they catalyze.  
        - Each EC number consists of four numbers separated by periods (e.g., `2.7.1.1`).  
        - The first number represents the main enzyme class (6 major classes: Oxidoreductases, Transferases, Hydrolases, Lyases, Isomerases, Ligases).  
        - The subsequent numbers give more specific subclass, sub-subclass, and the serial number of the enzyme.  
        """)
    with st.sidebar.expander("Why is it relevant?", expanded=False):
        st.markdown("""
        EC numbers tell us **what each enzyme in a LAB can do**.
        For example:  
        - Which sugars or fibers the bacteria can break down  
        - Which beneficial compounds (like vitamins or organic acids) they might produce  
        - How they might interact in food or the gut  
    So EC numbers help in **connecting the functional predictions from PICRUSt to real biological activities**.
        """)
    with st.sidebar.expander("What is in the EC Dataframe?", expanded=False):
        st.markdown("""
    Here's what each column represents:
    - **ec_number**: The Enzyme Commission (EC) number classifying the enzyme's activity.
    - **ec_abundance**: How many times this enzyme is predicted to be present in the strain.
    - **ec_function**: Description of the enzyme's function.
    - **ec_class**: The main EC class (number 1–6) the enzyme belongs to.
    - **ec_class_name**: The name of the EC class (e.g., Transferases, Hydrolases).
    - **ko_ids**: KEGG Orthology IDs linked to this enzyme.
    - **ko_functions**: Descriptions of the KO functions linked to this enzyme.
    - **pathway_ids**: KEGG pathway IDs associated with this enzyme.
    - **pathway_names**: Names of the KEGG pathways this enzyme participates in.
    - **brite_subclass**: KEGG BRITE hierarchy subclass for this enzyme.
    - **brite_class**: KEGG BRITE hierarchy main class for this enzyme.
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
    with st.sidebar.expander("What is a KO ID?", expanded=False):
    st.markdown("""
    **KO (KEGG Orthology) IDs** represent groups of genes/proteins that have the **same functional role** in different organisms.  
    - Each KO ID corresponds to a specific **orthologous gene** in the KEGG database.  
    - KOs help in linking **genes to metabolic pathways** and **enzyme functions**.  
    """)

    with st.sidebar.expander("Why is it relevant?", expanded=False):
        st.markdown("""
        KO IDs are important because they tell us **what functions a LAB strain may carry out at the gene level**.  
        For example:  
        - Which transporters, enzymes, or proteins are present  
        - Which metabolic or signaling pathways the strain may be capable of  
        - How the predicted functions relate to **probiotic and food applications**  
    In this app, KO IDs help connect **genomic predictions to real biological activities** and link them to EC numbers and pathways.
        """)
    
    with st.sidebar.expander("What is in the KO Dataframe?", expanded=False):
        st.markdown("""
        Here's what each column in the KO dataframe represents:
        - **ko_id**: KEGG Orthology ID for a gene/protein with a specific function.
        - **ko_abundance**: Number of times this KO is predicted in the strain.
        - **ko_function**: Description of the KO’s functional role.
        - **ec_id**: Associated EC number(s) for this KO (if available).
        - **ec_class**: The EC class of the linked enzyme.
        - **ec_function**: Function of the linked enzyme.
        - **map_ids**: KEGG pathway map IDs associated with this KO.
        - **pathway_names**: Names of KEGG pathways this KO participates in.
        - **brite_subclass**: KEGG BRITE hierarchy subclass for this KO.
        - **brite_class**: KEGG BRITE hierarchy main class for this KO.
        - **ec_abundance**: Abundance of the linked EC(s).
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
