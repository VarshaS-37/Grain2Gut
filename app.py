import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from upsetplot import UpSet, from_memberships
from itertools import combinations

st.set_page_config(layout="wide")

# ----------------------------------------------------------------- CSS -----------------------------------------------------------------
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
# ------------------------------------------------footer----------------------------------------------------------------------------------
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

# ----------------------------------------------------------- Page Control -------------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to(page):
    st.session_state.page = page
    st.rerun()

# ------------------------------------------------------------ Home Page -----------------------------------------------------------------------
def home():
    st.markdown("<h2 style='text-align:center;'>Grain2Gut</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;'><i>Linking genomic potential of Millet derived Lactic Acid Bacteria to food and probiotic applications</i></h4>", unsafe_allow_html=True)
    st.write("") 
    # ----------------------------------- Sidebar with Project Description ------------------------------------------------------------------------
   # "Back to Home" button at the top of the sidebar
    
    with st.sidebar.expander("About This App", expanded=False):
        st.markdown("""
        1. This app is based on a research paper by our guide, where lactic acid bacteria (LAB) were isolated and characterized from millets([research paper link](https://github.com/VarshaS-37/Grain2Gut/blob/main/Isolation_%26_characterization_of_biological_traits_of_millet-derived_lactic_acid_bacteria.pdf)).
        2. Among the isolates, four LAB strains showed probiotic characteristics, and their 16S rRNA partial sequences were submitted to NCBI.
        3. These sequences have been used for functional prediction using PICRUSt (Phylogenetic Investigation of Communities by Reconstruction of Unobserved States).
        4. The raw PICRUSt outputs were processed to obtain KO (KEGG Orthology), EC (Enzyme Commission), and PWY (Pathway) dataframes.
        5. Each dataframe was independently linked to reference information from databases.
        """)
    with st.sidebar.expander("Summarized Analysis", expanded=False):
        st.markdown("""
        This contains the overall summary of our results.
        """)
    with st.sidebar.expander("Millet-wise Analysis", expanded=False):
        st.markdown("""
        This contains the detailed analysis and functional comparison across millets.
        """)
    with st.sidebar.expander("Meta Data", expanded=False):
        st.markdown("""
        This contains all the processed dataframes created from the raw files and are used for further analysis.
        """)
     
   
    left_col, middle_col, right_col = st.columns([1, 1, 1])  # left & middle for extra buttons/spaces, right for Detailed Analysis
    
    # -------------------------------------------------Summarized Analysis-------------------------------------------------------------
    with left_col:
        if st.button("Summarized Analysis"):
            go_to("summarized_analysis")
    # ------------------------------------------------Millet-wise Analysis---------------------------------------------------------------
    with middle_col:
        if st.button("Millet-wise Analysis"):
            go_to("milletwise_analysis")
   # -------------------------------------------------- Meta Data ---------------------------------------------------------------------------
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
     
# -------------------------------------------------- Millet Data Mapping -------------------------------------------------------------------
millet_map = {
    "Enterococcus casseliflavus (Proso Millet)": "77",
    "Weisella cibaria NM01 (Foxtail Millet)": "78",
    "Weisella cibaria NM01 (Little Millet)": "79",
    "Lactococcus lactis (Little Millet)": "80"
}
# ---------------------------------------------------- EC Analysis ------------------------------------------------------------------------------
def ec_page():
    st.markdown("<h3 style='text-align:center;'>EC Analysis</h3>", unsafe_allow_html=True)
     # ------------------------------------------ Sidebar with instructions -----------------------------------------------------
    with st.sidebar:
        if st.button("Back to Home"):
            go_to("home")  # Your navigation function
        with st.sidebar.expander("How to Use this Page", expanded=False):
            st.markdown("""
            **Instructions:**
            1. Select the millet LAB from the dropdown at the top.
            2. On the left, the entire EC dataframe for the selected LAB is displayed.
            3. Use the **EC number dropdown** above the dataframe to select an EC number.
            4. The right column will show the textual interpretation for the selected EC number.
            5. Use the **"Back to Home"** button at the bottom to return to the home page.
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
            1. Only EC numbers with abundance greater than 1 are considered.
            2. Here's what each column means:
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
    #--------------------------------------------------------Select LAB----------------------------------------------------------------------
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
        df = pd.read_csv(f"picrust_processed_output_files/ec{suffix}.csv")
    except FileNotFoundError:
        st.error(f"File ec{suffix}.csv not found.")
        return

    # Load textual interpretation CSV
    try:
        text_df = pd.read_csv(f"picrust_processed_output_files/ec{suffix}_text.csv", encoding='ISO-8859-1')  # columns: ec_number, description
    except FileNotFoundError:
        st.error(f"Text file ec{suffix}_text.csv not found.")
        return
    st.write("")  # spacing

    # ----------------------------------------------- Side-by-Side Columns ---------------------------------------------------------------------------
    left_col, right_col = st.columns([1, 2])  # left smaller, right bigger

    # ----------------------------------- Left Column: EC number dropdown + Full EC DataFrame ----------------------------------------------------
    with left_col:
        st.markdown("<h4 style='text-align:center;'>Select a EC Number</h4>", unsafe_allow_html=True)
        if 'ec_number' in df.columns:
            selected_ec = st.selectbox("",df['ec_number'].unique(), label_visibility="collapsed",key="ec_select")
        else:
            st.warning("Column 'ec_number' not found in dataframe.")
            selected_ec = None
        st.markdown("<h4 style='text-align:center;'>EC DataFrame</h4>", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)

    # -------------------------------------------- Right Column: Textual Interpretation -------------------------------------------------------
    with right_col:
        st.markdown("<h4 style='text-align:center;'>Interpretation</h4>", unsafe_allow_html=True)
        if selected_ec:
            ec_text = text_df[text_df['ec_number'] == selected_ec]
            if not ec_text.empty:
                # Display EC number in larger bold font
                st.markdown(f"<h3 style='text-align:center;'>{selected_ec}</h3>", unsafe_allow_html=True)
                # Split the description by semicolon
                description = ec_text.iloc[0]['description']
                parts = [part.strip() for part in description.split(';')]
                for part in parts:
                    # Split at the first colon to bold the section title
                    if ':' in part:
                        title, text = part.split(':', 1)
                        st.markdown(f"<p style='font-size:16px;'><strong>{title}:</strong> {text.strip()}</p>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<p style='font-size:16px;'>{part}</p>", unsafe_allow_html=True)
            else:
                st.warning("No textual description found for this EC number.")


    
  
# --------------------------------------------------- KO Page: Side-by-Side + Sidebar -------------------------------------------------------------
def ko_page():
    st.markdown("<h3 style='text-align:center;'>KO Analysis</h3>", unsafe_allow_html=True)
    # ------------------------------------- Sidebar with instructions ----------------------------------------------------------------------
    with st.sidebar:
        if st.button("Back to Home"):
            go_to("home")  # Your navigation function
        with st.sidebar.expander("How to Use this Page", expanded=False):
            st.markdown("""
            **Instructions:**
            1. Select the millet LAB from the dropdown at the top.
            2. On the left, the entire KO dataframe for the selected LAB is displayed.
            3. Use the **KO ID dropdown** above the dataframe to select a KO ID.
            4. The right column will show the textual interpretation for the selected KO number.
            5. Use the **"Back to Home"** button at the bottom to return to the home page.
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
            1. Only KO ids with abundance greater than 2 are considered.
            2. Here's what each column in the KO dataframe means:
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
    # ------------------------------------------ Millet LAB Selection --------------------------------------------------------------------------
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
    # Load KO DataFrame
    try:
        df = pd.read_csv(f"picrust_processed_output_files/ko{suffix}.csv")
    except FileNotFoundError:
        st.error(f"File ko{suffix}.csv not found.")
        return
    # Load textual interpretation CSV
    try:
        text_df = pd.read_csv(f"picrust_processed_output_files/ko{suffix}_text.csv", encoding='ISO-8859-1')  # columns: ko_number, description
    except FileNotFoundError:
        st.error(f"Text file ko{suffix}_text.csv not found.")
        return
    st.write("")  # spacing
    # ------------------------------------------------- Side-by-Side Columns ---------------------------------------------------------------------------
    left_col, right_col = st.columns([1, 2])  # left smaller, right bigger
    # ---------------------------------------- Left Column: KO number dropdown + Full KO DataFrame ----------------------------------------------
    with left_col:
        st.markdown("<h4 style='text-align:center;'>Select a KO ID</h4>", unsafe_allow_html=True)
        if 'ko_id' in df.columns:
            selected_ko = st.selectbox("", df['ko_id'].unique(), label_visibility="collapsed",key="ko_select")
        else:
            st.warning("Column 'ko_number' not found in dataframe.")
            selected_ko = None
        st.markdown("<h4 style='text-align:center;'>KO DataFrame</h4>", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)
    # ---------------------------------------- Right Column: Textual Interpretation -------------------------------------------------------------
    with right_col:
        st.markdown("<h4 style='text-align:center;'>Interpretation</h4>", unsafe_allow_html=True)
        if selected_ko:
            ko_text = text_df[text_df['ko_id'] == selected_ko]
            if not ko_text.empty:
                # Display KO ID in larger bold font
                st.markdown(f"<h3 style='text-align:center;'>{selected_ko}</h3>", unsafe_allow_html=True)
                # Split the description by semicolon
                description = ko_text.iloc[0]['description']
                parts = [part.strip() for part in description.split(';')]
                for part in parts:
                    # Split at the first colon to bold the section title
                    if ':' in part:
                        title, text = part.split(':', 1)
                        st.markdown(f"<p style='font-size:16px;'><strong>{title}:</strong> {text.strip()}</p>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<p style='font-size:16px;'>{part}</p>", unsafe_allow_html=True)
            else:
                st.warning("No textual description found for this KO ID.")
   
# --------------------------------------------------- Pathway Page: Side-by-Side + Sidebar ----------------------------------------------------------
def pwy_page():
    st.markdown("<h3 style='text-align:center;'>Pathway Analysis</h3>", unsafe_allow_html=True)
    # ---------------------------------------------------- Sidebar with instructions ------------------------------------------------------------------
    with st.sidebar:
        if st.button("Back to Home"):
            go_to("home")  # Your navigation function
        with st.sidebar.expander("How to Use this Page", expanded=False):
            st.markdown("""
            **Instructions:**
            1. Select the millet LAB from the dropdown at the top.
            2. On the left, the entire pathway dataframe for the selected LAB is displayed.
            3. Use the **Pathway ID dropdown** above the dataframe to select a pathway.
            4. The right column will show the textual interpretation for the selected pathway.
            5. Use the **"Back to Home"** button at the bottom to return to the home page.
            """)
        with st.sidebar.expander("What is a Pathway?", expanded=False):
            st.markdown("""
            **Pathways** represent a series of biochemical reactions or processes that occur in the cell, often involving multiple enzymes and genes.  
            """)
        with st.sidebar.expander("Why is it relevant?", expanded=False):
            st.markdown("""
            Pathway analysis shows **how the predicted enzymes and genes work together** in biological processes.  
            This helps us understand:  
            - Which **metabolic or biosynthetic pathways** are present in the LAB strain  
            - How complete these pathways are  
            - The potential **functional and probiotic properties** of the strain
            """)
        with st.sidebar.expander("What is in the Pathway Dataframe?", expanded=False):
            st.markdown("""
            1. Only pathways with completeness greater than 0.79 are considered.
            2. Here's what each column in the dataframe means:
            - **Pathway**: Unique pathway ID in the database (e.g., `ANAGLYCOLYSIS-PWY`).  
            - **fam_total**: Total number of gene families expected in this pathway.  
            - **fam_found**: Number of gene families found in the LAB strain for this pathway.  
            - **completeness**: Fraction of the pathway that is present (0–1), calculated as `fam_found / fam_total`.  
            - **pathway_name**: Descriptive name of the pathway (e.g., `glycolysis III (from glucose)`).  
            """)
    # ---------------------------------------------- Millet LAB Selection -------------------------------------------------------------------
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
    # Load Pathway DataFrame
    try:
        df = pd.read_csv(f"picrust_processed_output_files/pwy_{suffix}.csv")
    except FileNotFoundError:
        st.error(f"File pwy_{suffix}.csv not found.")
        return
    # Load textual interpretation CSV
    try:
        text_df = pd.read_csv(f"picrust_processed_output_files/pwy{suffix}_text.csv")  # columns: pathway_id, description
    except FileNotFoundError:
        st.error(f"Text file pwy{suffix}_text.csv not found.")
        return
    st.write("")  # spacing
    # ---------------------------------------------------- Side-by-Side Columns -----------------------------------------------------------------
    left_col, right_col = st.columns([1, 2])  # left smaller, right bigger
    # ------------------------------------- Left Column: Pathway ID dropdown + Full Pathway DataFrame -------------------------------------------------
    with left_col:
        st.markdown("<h4 style='text-align:center;'>Select a Pathway</h4>", unsafe_allow_html=True)
        if 'Pathway' in df.columns:
            selected_pwy = st.selectbox("", df['Pathway'].unique(), label_visibility="collapsed",key="pwy_select")
        else:
            st.warning("Column 'pathway_id' not found in dataframe.")
            selected_pwy = None
        st.markdown("<h4 style='text-align:center;'>Pathway DataFrame</h4>", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)
    # -------------------------------------------- Right Column: Textual Interpretation -------------------------------------------------------
    with right_col:
        st.markdown("<h4 style='text-align:center;'>Interpretation</h4>", unsafe_allow_html=True)
        if selected_pwy:
            pwy_text = text_df[text_df['Pathway'] == selected_pwy]
            if not pwy_text.empty:
                # Display Pathway ID in larger bold font
                st.markdown(f"<h3 style='text-align:center;'>{selected_pwy}</h3>", unsafe_allow_html=True)
                # Split the description/interpretation by semicolon (if available)
                description = pwy_text.iloc[0]['description']  # make sure your dataframe has a 'description' column
                parts = [part.strip() for part in description.split(';')]
                for part in parts:
                    # Split at first colon to bold section titles
                    if ':' in part:
                        title, text = part.split(':', 1)
                        st.markdown(f"<p style='font-size:16px;'><strong>{title}:</strong> {text.strip()}</p>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<p style='font-size:16px;'>{part}</p>", unsafe_allow_html=True)
            else:
                st.warning("No textual description found for this pathway.")
    
#---------------------------------------------------millet analysis --------------------------------------------------------------------------
def millet():
    st.markdown("<h4 style='text-align:center;'>Millet-wise Analysis</h4>", unsafe_allow_html=True)
    with st.sidebar:
        if st.button("Back to Home"):
            go_to("home") 
        with st.sidebar.expander("Millet Data", expanded=False):
            st.markdown("""
            Contains data about the four millet derived LAB used and their NCBI links are provided.
            """)
        with st.sidebar.expander("EC class Distribution", expanded=False):
            st.markdown("""Shows the distribution of EC numbers across the six major EC classes for each millet.""")
        with st.sidebar.expander("BRITE class & subclass Distribution", expanded=False):
            st.markdown("""
            - For each EC number & KO id, multiple map ids (pathway ids) are retrieved.
            - These map ids are then mapped to their BRITE class & subclasses whose distribution across each millet is plotted.
            """)
        with st.sidebar.expander("Biological Trait Distribution", expanded=False):
            st.markdown("""
            - Based on our understanding of all the data, we have assigned biological traits to each EC, KO, PWY.
            - Their distribution is plotted for each millet.
            """)
        with st.sidebar.expander("Common & Unique Traits", expanded=False):
            st.markdown("""
            - The assigned biological traits are compared across millets.
            - The common and unique traits across millets are plotted here.
            """)
        with st.sidebar.expander("Pathway Enrichment", expanded=False):
            st.markdown("""
            Pathway enrichment helps identify **which biological pathways are more represented or more active** in one LAB strain **compared to others**.
            """)
    millet_data = {
        "Millet Source": ["Proso", "Foxtail", "Little", "Little"],
        "Strain": ['BM01', 'NM01', 'SM01', 'SM02'],
        "Organism": [
            "Enterococcus casseliflavus", 
            "Weissella cibaria", 
            "Weissella cibaria", 
            "Lactococcus lactis"
        ],
        "NCBI ID": ['PP355677', 'PP355678', 'PP355679', 'PP355680'],
        "NCBI Link": [
            "https://www.ncbi.nlm.nih.gov/nuccore/PP355677.1/", 
            "https://www.ncbi.nlm.nih.gov/nuccore/pp355678", 
            "https://www.ncbi.nlm.nih.gov/nuccore/pp355679",
            "https://www.ncbi.nlm.nih.gov/nuccore/pp355680"] 
    }
    millet_df = pd.DataFrame(millet_data)
    left_col, right_col = st.columns([2, 2]) 
    with left_col:
        st.markdown("<h4 style='text-align:center;'>Millet Data</h4>", unsafe_allow_html=True)
        st.data_editor(
            millet_df,
            column_config={
                "NCBI Link": st.column_config.LinkColumn(
                    "NCBI Link",
                    display_text="NCBI Link" 
                ),
            },
            hide_index=True,
            use_container_width=True
        )
    with right_col:
        st.markdown("<h4 style='text-align:center;'>Analysis</h4>", unsafe_allow_html=True)
        col1, col2,col3 = st.columns(3)
        with col1:
            if st.button("EC class Distribution"):
                go_to("ec_class")
        with col2:
            if st.button("BRITE class & subclass Distribution"):
                go_to("brite")
        with col3:
            if st.button("Trait Distribution"):
                go_to("trait")        
        col4, col5,col6= st.columns(3)
        with col4:
            if st.button("Common & Unique EC classes"):
                go_to("cocl")
        with col5:
            if st.button("Common & Unique BRITE classes and subclasses"):
                go_to("brcl")
        with col6:
            if st.button("Common & Unique Traits"):
                go_to("couq")
        col7, col8,col9= st.columns([3,3,3])
        with col8:
            if st.button("Pathway Enrichment"):
                go_to("pe")       
#--------------------------------------ec class------------------------------------------------------------------------------------------------
def ec_class():
    with st.sidebar:
        if st.button("Back to Home"):
            go_to("home")
        if st.button("Back to Analysis Menu"):
            go_to("milletwise_analysis")    
        with st.sidebar.expander("What are the major EC classes?", expanded=False):
            st.markdown("""
            1. **Oxidoreductases (EC 1):** Catalyzes redox reactions, moves electrons between molecules.  
            2. **Transferases (EC 2):** Moves functional groups from one molecule to another.  
            3. **Hydrolases (EC 3):** Breaks molecules using water.  
            4. **Lyases (EC 4):** Breaks bonds in molecules without water or oxidation.  
            5. **Isomerases (EC 5):** Rearranges molecules into different forms.  
            6. **Ligases (EC 6):** Joins two molecules together using energy.
            """)
        with st.sidebar.expander("How are they relevant?", expanded=False):
            st.markdown("""
            The presence of these enzymes implies their diverse functional capabilities related to food fermentation and probiotic activity:
        
            1. **Oxidoreductases (EC 1):** Helps in fermentation, making acids, and giving antioxidant benefits.  
            2. **Transferases (EC 2):** Helps in making vitamins and amino acids that improve nutrition.  
            3. **Hydrolases (EC 3):** Helps in breaking food molecules, improving digestibility, and releasing helpful compounds.  
            4. **Lyases (EC 4):** Helps in forming flavor compounds and allowing flexible use of nutrients.  
            5. **Isomerases (EC 5):** Helps in changing sugars and amino acids into useful forms and making prebiotics.  
            6. **Ligases (EC 6):** Helps in bacterial growth and stability in foods.
            """)

    col1, col2, col3 = st.columns([3, 3, 3])
    with col2:
        st.markdown("<h4 style='text-align:center;'>EC class Distribution</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align:center;'>Select the Millet LAB</h4>", unsafe_allow_html=True)
        selected_strain = st.selectbox(
            "",
            list(millet_map.keys()),
            label_visibility="collapsed",
            key=f"ec_class_select_{st.session_state.page}",
        )
    suffix = millet_map[selected_strain]
    # ---- EC DISTRIBUTION ----
    try:
        # Load EC CSV from local folder
        df = pd.read_csv(f"picrust_processed_output_files/ec{suffix}.csv")
    except FileNotFoundError:
        st.error(f"File ec{suffix}.csv not found in 'picrust_processed_output_files/' folder.")
        return
    # Validate presence of required column
    if "ec_class_name" not in df.columns:
        st.warning(f"'ec_class_name' column not found in ec{suffix}.csv.")
        return
    # Count enzymes by EC class
    class_counts = df["ec_class_name"].value_counts().reset_index()
    class_counts.columns = ["EC Class", "Count"]
# --- Layout: Left (figure) + Right (interpretation) ---
    left_col, right_col = st.columns([2, 2])

    with left_col:
        # Plot EC class distribution
        fig, ax = plt.subplots(figsize=(6, 4))
        bars=ax.bar(class_counts["EC Class"], class_counts["Count"], color="#4C72B0")
        ax.set_xlabel("EC Class", fontsize=10)
        ax.set_ylabel("Number of Enzymes", fontsize=10)
        ax.set_title(f"EC Class Distribution - {selected_strain}", fontsize=12)
        plt.xticks(rotation=45, ha="right")
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height, str(int(height)),ha='center', va='bottom', fontsize=9)
        plt.tight_layout()
        st.pyplot(fig)

    with right_col:
        st.markdown("<h4 style='text-align:center;'>Interpretation</h4>", unsafe_allow_html=True)
        st.write(f"""
        - **Dominant EC classes:** {', '.join(class_counts['EC Class'].head(3).tolist())}
        """)
#-----------------------------------------------------------brite class-------------------------------------------------------------------
def brite_class():
    # ... your sidebar code ...
    st.markdown("<h4 style='text-align:center;'>BRITE class & subclass Distribution</h4>", unsafe_allow_html=True)
    with st.sidebar:
        if st.button("Back to Home"): 
            go_to("home") 
        if st.button("Back to Analysis Menu"):
            go_to("milletwise_analysis") 
    with st.sidebar.expander("What is a BRITE class?", expanded=False): 
        st.markdown("""
        - BRITE classes are top-level functional categories in the KEGG database.  
        - They group genes, proteins, and pathways based on broad biological roles, such as enzymes, transporters, or signaling proteins.
        """, unsafe_allow_html=True)
    with st.sidebar.expander("What is a BRITE subclass?", expanded=False): 
        st.markdown("""
        - BRITE subclasses are more specific categories within each BRITE class.  
        - They further organize proteins or pathways by detailed functions, like specific enzyme families, types of transporters, or metabolic pathways.
        """, unsafe_allow_html=True)
    with st.sidebar.expander("Why are they relevant?", expanded=False): 
        st.markdown("""
        - Helps identify enzymes and pathways that probiotic bacteria can use to metabolize food components.
        - Shows which bioactive compounds (vitamins, organic acids, peptides) they might produce.
        - Reveals mechanisms for survival and interaction</b> in food or the gut, like stress response or nutrient transport.
        """, unsafe_allow_html=True)

 
    col1, col2, col3 = st.columns([3, 3, 3]) 
    with col2:
        st.write("")
        st.markdown("<h5 style='text-align:center;'>Select distribution category</h5>", unsafe_allow_html=True)
        selected_dist = st.selectbox(
            "",
            ['EC Distribution','KO Distriution'],
            label_visibility="collapsed",
            key=f"brite_class_select_{st.session_state.page}",
        )
        st.markdown("<h5 style='text-align:center;'>Select the Millet LAB</h5>", unsafe_allow_html=True)
        selected_strain = st.selectbox(
            "",
            list(millet_map.keys()),
            label_visibility="collapsed",
            key=f"pwy_strain_select_{st.session_state.page}",
        )
    suffix = millet_map[selected_strain]
    try:
        df = pd.read_csv(f"picrust_processed_output_files/{selected_dist[0:2].lower()}{suffix}.csv")
    except FileNotFoundError:
        st.error(f"File {selected_dist[0:2].lower()}{suffix}.csv not found.")
        return
    
    # Validate columns
    required_cols = ["brite_class", "brite_subclass"]
    for col in required_cols:
        if col not in df.columns:
            st.warning(f"'{col}' column not found in the CSV.")
            return

  # --- Split semicolon-separated entries and count ---
    # Brite Class
    class_counts = (
        df["brite_class"].dropna().str.split(";").explode().str.strip().value_counts()
    )
    class_counts = class_counts[class_counts >= 3]  # Keep only counts >= 3
    class_counts = class_counts.reset_index()
    class_counts.columns = ["Brite Class", "Count"]
    
    # Brite Subclass
    subclass_counts = (
        df["brite_subclass"].dropna().str.split(";").explode().str.strip().value_counts()
    )
    subclass_counts = subclass_counts[subclass_counts >= 3]  # Keep only counts >= 3
    subclass_counts = subclass_counts.reset_index()
    subclass_counts.columns = ["Brite Subclass", "Count"]

    left_col, right_col = st.columns([2, 2])
    with left_col:
        fig, ax = plt.subplots(figsize=(6, 4))
        bars=ax.bar(class_counts["Brite Class"], class_counts["Count"], color="#4C72B0")
        ax.set_xlabel("Brite Class")
        ax.set_ylabel("Count")
        ax.set_title(f"Brite Class Distribution - {selected_strain}")
        plt.xticks(rotation=45, ha="right")
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height, str(int(height)), ha='center', va='bottom', fontsize=9)
        plt.tight_layout()
        st.pyplot(fig)
    with right_col:
        fig, ax = plt.subplots(figsize=(6, 4))
        bars=ax.bar(subclass_counts["Brite Subclass"], subclass_counts["Count"], color="#4C72B0")
        ax.set_xlabel("Brite Subclass")
        ax.set_ylabel("Count")
        ax.set_title(f"Brite Subclass Distribution - {selected_strain}")
        plt.xticks(rotation=45, ha="right")
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height, str(int(height)),ha='center', va='bottom', fontsize=9)
        plt.tight_layout()
        st.pyplot(fig)
        
#----------------------------------------------------trait distribution--------------------------------------------------------------------------------            
def trait():
    st.markdown("<h4 style='text-align:center;'>Biological Trait Distribution</h4>", unsafe_allow_html=True)
    with st.sidebar:
        if st.button("Back to Home"): 
            go_to("home") 
        if st.button("Back to Analysis Menu"):
            go_to("milletwise_analysis") 
    with st.sidebar.expander("Why are they relevant?", expanded=False): 
        st.markdown("""
        By assigning biological traits, we can predict how a LAB may behave in food or in the gut,  
        which helps identify **better LAB strains** for use in food applications.
        """, unsafe_allow_html=True)
 
    col1, col2, col3 = st.columns([3, 3, 3]) 
    with col2:
        st.write("")
        st.markdown("<h5 style='text-align:center;'>Select distribution category</h5>", unsafe_allow_html=True)
        selected_dist = st.selectbox(
            "",
            ['EC Traits','KO Traits','PWY Traits'],
            label_visibility="collapsed",
            key=f"brite_class_select_{st.session_state.page}",
        )
        st.markdown("<h5 style='text-align:center;'>Select the Millet LAB</h5>", unsafe_allow_html=True)
        selected_strain = st.selectbox(
            "",
            list(millet_map.keys()),
            label_visibility="collapsed",
            key=f"pwy_strain_select_{st.session_state.page}",
        )
    suffix = millet_map[selected_strain]
    try:
        df = pd.read_csv(f"picrust_processed_output_files/{selected_dist.split(' ')[0].lower()}{suffix}_word.csv")
    except FileNotFoundError:
        st.error(f"File {selected_dist.strip(' ')[0].lower()}{suffix}.csv not found.")
        return
    
    # Validate columns
    if 'trait' not in df.columns:
        st.warning("trait column not found in the CSV.")
        return
    trait_counts = (
        df["trait"].dropna().value_counts()
    )
    trait_counts = trait_counts[trait_counts >= 2]  # Keep only counts >= 3
    trait_counts = trait_counts.reset_index()
    trait_counts.columns = ["Trait", "Count"]
    
    fig, ax = plt.subplots(figsize=(6, 4))
    bars=ax.bar(trait_counts["Trait"], trait_counts["Count"], color="#4C72B0")
    ax.set_xlabel("Trait")
    ax.set_ylabel("Count")
    ax.set_title(f"Trait Distribution - {selected_strain}")
    plt.xticks(rotation=45, ha="right")
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height, str(int(height)), ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)
#-------------------------------------------------common & unique-----------------------------------------------------------------------------
def couq():
    with st.sidebar:
        if st.button("Back to Home"): 
            go_to("home") 
        if st.button("Back to Analysis Menu"):
            go_to("milletwise_analysis") 

    with st.sidebar.expander("Why is this relevant?", expanded=False): 
        st.markdown("""
        - Common traits indicates shared core metabolic functions and probiotic capabilities.
        - Unique traits indicates special metabolic or adaptive features linked to each millet.""")
    with st.sidebar.expander("What is an Upset plot?", expanded=False): 
        st.markdown("""     
        - An **UpSet Plot** is a visualization used to compare **overlaps between multiple groups**.  
        - Here, it is used to compare **functional traits** (EC, KO, Pathway features) across the **four millet-derived LAB strains**.
        - It serves a similar purpose as a **Venn diagram**, but works much better when comparing **more than 3 groups**.
        """)
    with st.sidebar.expander("How to Read the UpSet Plot?", expanded=False): 
        st.markdown("""    
        The plot has two main parts:
        ### 1) Dot Matrix (Bottom Panel)
        This shows **which strain combinations are being compared**.
        
        | Pattern | Meaning |
        |--------|---------|
        | ● A single dot under one strain | Trait is **unique** to that strain |
        | ● ● Two dots connected by a line | Trait is **shared** between those two strains |
        | ● ● ● Three connected dots | Trait is **shared by three strains** |
        | ● ● ● ● All four connected dots | Trait is **common to all four LAB strains** |
        
        So, **the dots tell *who shares the trait*.**
        
        ---
        
        ### 2) Vertical Bars (Top Panel)
        The **bar height** tells **how many traits** fall into that particular combination.
        
        | Bar Height | Interpretation |
        |------------|----------------|
        | Tall Bar | Many traits in that group/overlap |
        | Short Bar | Fewer traits in that group/overlap |
        
        So:
        - A **tall bar with all dots connected** = Many **core shared traits**
        - A **tall bar with only one dot** = Many **unique traits for that strain**
         ### 3) Left Vertical Bars (Side Panel)
    The **bars on the left side of the plot** indicate the **total number of traits per millet strain**.
        """)

    st.write('')
    st.markdown(f"<h5 style='text-align:center;'>Common & Unique traits</h5>", unsafe_allow_html=True) 
    from itertools import combinations
    millet_sets={}
    # Combine EC, KO, PWY for each millet LAB
    for strain_name, suffix in millet_map.items():
        combined_traits = set()
        files = [f"ec{suffix}_word.csv", f"ko{suffix}_word.csv", f"pwy{suffix}_word.csv"]
        for f in files:
            try:
                df = pd.read_csv(f"picrust_processed_output_files/{f}")
                if "trait" in df.columns:
                    combined_traits.update(df["trait"].dropna().unique())
            except FileNotFoundError:
                st.warning(f"File {f} not found, skipping.")
        millet_sets[strain_name] = combined_traits

    from upsetplot import UpSet, from_memberships
   

    # millet_sets: dict of millet_name -> set of traits
    memberships = []
    for millet, traits in millet_sets.items():
        for trait in traits:
            memberships.append((trait, millet))
    
    # Create the UpSet data
    data = from_memberships(
        [[millet for millet in millet_sets if trait in millet_sets[millet]] for trait in set.union(*millet_sets.values())]
    )
    
    fig = plt.figure(figsize=(8,6))
    upset = UpSet(data, subset_size='count', show_counts=True)
    upset.plot(fig=fig)  # pass the figure explicitly
    st.pyplot(fig)


    # --- Common to all 4 LABs ---
    common_4 = set.intersection(*millet_sets.values())
    st.markdown(f"<h5 style='text-align:center;'>Traits Common to All 4 Millets</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame({"Trait": sorted(common_4)}))

    unique_rows = []
    for millet, traits in millet_sets.items():
        # union of all traits in *other* millets
        other_traits = set.union(*(t for m, t in millet_sets.items() if m != millet))
        unique_traits = traits - other_traits  # traits found only in this millet
        for trait in sorted(unique_traits):
            unique_rows.append({"Millet": millet, "Trait": trait})
    
    st.markdown(f"<h5 style='text-align:center;'>Unique Traits</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(unique_rows))
    
    # --- Common to exactly 3 LABs ---
    common_3_rows = []
    for combo in combinations(millet_sets.keys(), 3):
        s1, s2, s3 = millet_sets[combo[0]], millet_sets[combo[1]], millet_sets[combo[2]]
        common_3 = (s1 & s2 & s3) - common_4  # remove traits in all 4
        for trait in sorted(common_3):
            common_3_rows.append({"Millets": " & ".join(combo), "Trait": trait})
    st.markdown(f"<h5 style='text-align:center;'> Traits Common to Exactly 3 Millets</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(common_3_rows))
    
    # --- Common to exactly 2 LABs ---
    common_2_rows = []
    for combo in combinations(millet_sets.keys(), 2):
        s1, s2 = millet_sets[combo[0]], millet_sets[combo[1]]
        common_2 = (s1 & s2) - common_4
        # remove traits in any common_3 combination
        for combo3 in combinations(millet_sets.keys(), 3):
            common_3 = set.intersection(*(millet_sets[c] for c in combo3)) - common_4
            common_2 -= common_3
        for trait in sorted(common_2):
            common_2_rows.append({"Millets": " & ".join(combo), "Trait": trait})
    st.markdown(f"<h5 style='text-align:center;'>Traits Common to Exactly 2 Millets</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(common_2_rows))
    
#------------------------------------------------------enrichment-------------------------------------------------------------------

from scipy.stats import fisher_exact
from statsmodels.stats.multitest import multipletests
import streamlit as st
import glob
import os

def pathway_enrichment():
    st.markdown("<h4 style='text-align:center;'>Combined EC–KO–PWY Pathway Enrichment</h4>", unsafe_allow_html=True)

    with st.sidebar:
        if st.button("Back to Home"): 
            go_to("home")
        if st.button("Back to Analysis Menu"):
            go_to("milletwise_analysis")
    with st.sidebar.expander("Why is it relevant?", expanded=False):
        st.markdown("""
        Instead of looking at single genes or enzymes individually, enrichment focuses on **whole biological processes**.  
        This helps reveal **functional abilities** of the strain, such as:
        - Stress tolerance
        - Fermentation efficiency
        - Vitamin / amino acid production
        - Probiotic survival traits
        """) 
    with st.sidebar.expander("How is it done?", expanded=False):
        st.markdown("""
        1. Pathway information obtained from **EC, KO, PWY** annotations for the selected millet-derived LAB strain is combined.
        2. Pathway frequencies from the remaining strains (background) is combined.
        3. **Fisher’s Exact Test** is performed to find pathways that occur:
           - **More frequently** in the selected strain than in the combined background strains.
        4. **FDR correction**  is applied for statistical validity.
        5. The **most enriched pathways** are displayed in a bar plot + table.
        """)
    with st.sidebar.expander("What is p-value?", expanded=False):
        st.markdown("""
        A **p-value** tells us how likely it is that the observed difference happened **by chance**.
        - **Small p-value** → Unlikely due to chance → **Result is meaningful**
        - **Large p-value** → Could easily happen randomly → **Not meaningful**

        ### Significance Rule (Common):
        - p-value < 0.05 → **Statistically significant**
        """)
    with st.sidebar.expander("What is FDR?", expanded=False):
        st.markdown("""     
        - When testing **many pathways at once**, some pathways may look significant **just by luck**.
        - **FDR (False Discovery Rate)** correction adjusts p-values to prevent **false positives**.
        - **FDR is the corrected p-value**
        - Lower FDR = **More reliable** result
        """)
    with st.sidebar.expander("How to Read the Plot?", expanded=False):
        st.markdown("""
        - The **X-axis** shows `-log10(FDR)` → higher value = **stronger enrichment**.
        - The **Y-axis** lists pathway names.
        - **Longer bars = pathways more uniquely abundant in the selected strain**.
       """)


    # --- Select Millet LAB ---
    col1, col2, col3 = st.columns([3, 3, 3])
    with col2:
        st.markdown("<p style='text-align:center;'>Select Millet LAB</p>", unsafe_allow_html=True)
        selected_strain = st.selectbox(
            "",
            list(millet_map.keys()),
            label_visibility="collapsed",
            key=f"combined_enrich_select_{st.session_state.page}",
        )

    suffix = millet_map[selected_strain]
    data_dir = "picrust_processed_output_files"

    # --- Collect all pathways from EC, KO, and PWY ---
    all_pathways = []

    for prefix in ["ec", "ko", "pwy"]:
        if prefix == "pwy":
            file_path = os.path.join(data_dir, f"pwy_{suffix}.csv")
        else:
            file_path = os.path.join(data_dir, f"{prefix}{suffix}.csv")

        if not os.path.exists(file_path):
            st.warning(f"File not found: {file_path}")
            continue

        df = pd.read_csv(file_path, encoding="utf-8", on_bad_lines="skip")

        # Identify correct column
        for col in ["pathway_ids", "map_ids", "Pathway"]:
            if col in df.columns:
                df[col] = (
                    df[col].astype(str)
                    .str.replace(" ", "")
                    .str.replace(";", ",")
                    .str.split(",")
                )
                all_pathways.extend(df[col].explode().dropna().tolist())
                break

    if not all_pathways:
        st.warning("No pathway data found for selected millet.")
        return

    millet_counts = pd.Series(all_pathways).value_counts()

    # --- Build background from all other millets ---
    background_pathways = []
    for prefix in ["ec", "ko", "pwy"]:
        if prefix == "pwy":
            files = glob.glob(os.path.join(data_dir, "pwy_*.csv"))
        else:
            files = glob.glob(os.path.join(data_dir, f"{prefix}*.csv"))

        for f in files:
            if f.endswith(f"{suffix}.csv"):  # skip current strain
                continue

            try:
                df_bg = pd.read_csv(f, encoding="utf-8", on_bad_lines="skip")
            except UnicodeDecodeError:
                df_bg = pd.read_csv(f, encoding="latin1", on_bad_lines="skip")

            for col in ["pathway_ids", "map_ids", "Pathway"]:
                if col in df_bg.columns:
                    df_bg[col] = (
                        df_bg[col].astype(str)
                        .str.replace(" ", "")
                        .str.replace(";", ",")
                        .str.split(",")
                    )
                    background_pathways.extend(df_bg[col].explode().dropna().tolist())
                    break

    if not background_pathways:
        st.warning("No background pathway data found.")
        return

    bg_counts = pd.Series(background_pathways).value_counts()

    # --- Fisher’s Exact Test for enrichment ---
    results = []
    for pwy, count_in_millet in millet_counts.items():
        count_in_bg = bg_counts.get(pwy, 0)
        table = [
            [count_in_millet, len(all_pathways) - count_in_millet],
            [count_in_bg, len(background_pathways) - count_in_bg]
        ]
        try:
            _, p = fisher_exact(table, alternative="greater")
        except ValueError:
            continue
        results.append({"Pathway": pwy, "Count": count_in_millet, "p-value": p})

    if not results:
        st.warning("No significant enrichment found.")
        return

    res_df = pd.DataFrame(results)
    res_df["FDR"] = multipletests(res_df["p-value"], method="fdr_bh")[1]
    res_df = res_df.sort_values("FDR")

    # --- Visualization ---
    top = res_df.head(15)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(top["Pathway"], -np.log10(top["FDR"]), color="#4C72B0")
    ax.set_xlabel("-log10(FDR)")
    ax.set_ylabel("Pathway")
    ax.set_title(f"Combined EC–KO–PWY Enrichment: {selected_strain}")
    ax.invert_yaxis()
    plt.tight_layout()
    st.pyplot(fig)

    # --- Table output ---
    st.subheader(f"Top Enriched Pathways in {selected_strain}")
    st.dataframe(res_df.head(25).style.format({"p-value": "{:.3e}", "FDR": "{:.3e}"}))
#----------------------------------------------common classes-----------------------------------------------------------------------------------------------
def cocl(millet_map):
    with st.sidebar:
        if st.button("Back to Home"): 
            go_to("home") 
        if st.button("Back to Analysis Menu"):
            go_to("milletwise_analysis") 

    with st.sidebar.expander("Why is this relevant?", expanded=False): 
        st.markdown("""
        - Common EC classes indicate shared core metabolic functions.
        - Unique EC classes indicate special enzymatic features linked to each millet.
        """)

    with st.sidebar.expander("What is an UpSet plot?", expanded=False): 
        st.markdown("""
        - An **UpSet Plot** shows overlaps between multiple groups.
        - Here, it compares **EC classes** across four millet-derived LAB strains.
        - It serves a similar purpose as a **Venn diagram**, but works much better when comparing **more than 3 groups**.
        """)
    with st.sidebar.expander("How to Read the UpSet Plot?", expanded=False): 
        st.markdown("""    
        The plot has two main parts for **EC classes**:
    
        ### 1) Dot Matrix (Bottom Panel)
        This shows **which millet-derived LAB strains share EC classes**.
        
        | Pattern | Meaning |
        |--------|---------|
        | ● A single dot under one strain | EC class is **unique** to that strain |
        | ● ● Two dots connected by a line | EC class is **shared** between those two strains |
        | ● ● ● Three connected dots | EC class is **shared by three strains** |
        | ● ● ● ● All four connected dots | EC class is **common to all four LAB strains** |
        
        So, **the dots tell *who shares the EC class*.**
    
        ### 2) Vertical Bars (Top Panel)
        The **bar height** tells **how many EC classes** fall into that particular combination.
        
        | Bar Height | Interpretation |
        |------------|----------------|
        | Tall Bar | Many EC classes in that group/overlap |
        | Short Bar | Fewer EC classes in that group/overlap |
        
        So:
        - A **tall bar with all dots connected** = Many **core shared EC classes**
        - A **tall bar with only one dot** = Many **unique EC classes for that strain**
    
        ### 3) Left Vertical Bars (Side Panel)
        The **bars on the left side of the plot** indicate the **total number of EC classes per millet strain**.
        """)
    st.write("")
    st.markdown("<h5 style='text-align:center;'>Common & Unique EC Classes</h5>", unsafe_allow_html=True)

    # Load EC classes for each millet
    millet_ec = {}
    for strain_name, suffix in millet_map.items():
        try:
            df = pd.read_csv(f"picrust_processed_output_files/ec{suffix}.csv")
            if "ec_class_name" in df.columns:
                millet_ec[strain_name] = set(df["ec_class_name"].dropna().unique())
            else:
                st.warning(f"'ec_class_name' column missing in ec{suffix}.csv")
        except FileNotFoundError:
            st.warning(f"File ec{suffix}.csv not found.")

    if not millet_ec:
        st.error("No EC class data loaded.")
        return

    # --- UpSet plot ---
    memberships = []
    for ec in set.union(*millet_ec.values()):
        members = [millet for millet in millet_ec if ec in millet_ec[millet]]
        memberships.append(members)

    fig = plt.figure(figsize=(8,6))
    upset = UpSet(data, subset_size='count', show_counts=True)
    upset.plot(fig=fig)  # pass the figure explicitly
    st.pyplot(fig)

    # --- Common to all 4 millets ---
    common_4 = set.intersection(*millet_ec.values())
    st.markdown("<h5 style='text-align:center;'>EC Classes Common to All 4 Millets</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame({"EC Class": sorted(common_4)}))

    # --- Unique EC classes ---
    unique_rows = []
    for millet, classes in millet_ec.items():
        other_classes = set.union(*(c for m, c in millet_ec.items() if m != millet))
        unique = classes - other_classes
        for ec in sorted(unique):
            unique_rows.append({"Millet": millet, "EC Class": ec})
    st.markdown("<h5 style='text-align:center;'>Unique EC Classes</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(unique_rows))

    # --- Common to exactly 3 millets ---
    common_3_rows = []
    for combo in combinations(millet_ec.keys(), 3):
        s1, s2, s3 = millet_ec[combo[0]], millet_ec[combo[1]], millet_ec[combo[2]]
        common_3 = (s1 & s2 & s3) - common_4
        for ec in sorted(common_3):
            common_3_rows.append({"Millets": " & ".join(combo), "EC Class": ec})
    st.markdown("<h5 style='text-align:center;'>EC Classes Common to Exactly 3 Millets</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(common_3_rows))

    # --- Common to exactly 2 millets ---
    common_2_rows = []
    for combo in combinations(millet_ec.keys(), 2):
        s1, s2 = millet_ec[combo[0]], millet_ec[combo[1]]
        common_2 = (s1 & s2) - common_4
        for combo3 in combinations(millet_ec.keys(), 3):
            common_3 = set.intersection(*(millet_ec[c] for c in combo3)) - common_4
            common_2 -= common_3
        for ec in sorted(common_2):
            common_2_rows.append({"Millets": " & ".join(combo), "EC Class": ec})
    st.markdown("<h5 style='text-align:center;'>EC Classes Common to Exactly 2 Millets</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(common_2_rows))
#-------------------brite-----------------------------------------------------------------------------------
def brt():
    selected_c = st.selectbox(
            "",
            ['BRITE Class','BRITE Sublass' ],
            label_visibility="collapsed",
            key=f"combined_enrich_select_{st.session_state.page}",)
    with st.sidebar:
        if st.button("Back to Home"):
            go_to("home")
        if st.button("Back to Analysis Menu"):
            go_to("milletwise_analysis")
        with st.sidebar.expander("Why is this relevant?", expanded=False): 
            st.markdown("""
            - **Brite classes** group enzymes by broad metabolic functions.  
            - **Brite subclasses** show more specific enzyme roles within each class.  
            - Shared classes indicate core fermentation functions; unique ones show special activities for each millet.
            """)
        with st.sidebar.expander("What is an UpSet plot?", expanded=False): 
            st.markdown(f"""
            - An **UpSet Plot** shows overlaps between multiple groups.
            - Here, it compares **{selected_c}** across four millet-derived LAB strains.
            - It serves a similar purpose as a **Venn diagram**, but works much better when comparing **more than 3 groups**.
            """)
        
        with st.sidebar.expander("How to Read the UpSet Plot?", expanded=False): 
            st.markdown(f"""    
            The plot has two main parts for **{selected_c}**:
            
            ### 1) Dot Matrix (Bottom Panel)
            This shows **which millet-derived LAB strains share {selected_c}**.
            
            | Pattern | Meaning |
            |--------|---------|
            | ● A single dot under one strain | {selected_c} is **unique** to that strain |
            | ● ● Two dots connected by a line | {selected_c} is **shared** between those two strains |
            | ● ● ● Three connected dots | {selected_c} is **shared by three strains** |
            | ● ● ● ● All four connected dots | {selected_c} is **common to all four LAB strains** |
            
            So, **the dots tell *who shares the {selected_c}*.**
        
            ### 2) Vertical Bars (Top Panel)
            The **bar height** tells **how many {selected_c} fall into that particular combination**.
            
            | Bar Height | Interpretation |
            |------------|----------------|
            | Tall Bar | Many {selected_c} in that group/overlap |
            | Short Bar | Fewer {selected_c} in that group/overlap |
            
            So:
            - A **tall bar with all dots connected** = Many **core shared {selected_c}**
            - A **tall bar with only one dot** = Many **unique {selected_c} for that strain**
        
            ### 3) Left Vertical Bars (Side Panel)
            The **bars on the left side of the plot** indicate the **total number of {selected_c} per millet strain**.
            """)

    st.write("")
    st.markdown(f"<h4 style='text-align:center;'>{selected_c} Overlap Across Millets</h4>", unsafe_allow_html=True)
    if selected_c=='BRITE Class':
        brcl()
    elif selected_c=='BRITE Sublass':
        brsc()
    
#-------------------------------------------------------------brite class n subclass--------------------------------------------------------------------------------
def brcl():
 
   
    millet_sets = {}
    for strain, suffix in millet_map.items():
        classes = set()
        for prefix in ["ec", "ko"]:
            filename = f"picrust_processed_output_files/{prefix}{suffix}.csv"
            try:
                df = pd.read_csv(filename)
                if "brite_class" in df.columns:
                    classes.update(df["brite_class"].dropna().str.split(";").explode().str.strip())
            except FileNotFoundError:
                st.warning(f"File {filename} not found, skipping.")
        millet_sets[strain] = classes

    # UpSet plot
    data = from_memberships(
        [[strain for strain in millet_sets if cls in millet_sets[strain]] for cls in set.union(*millet_sets.values())]
    )
    fig = plt.figure(figsize=(8,6))
    upset = UpSet(data, subset_size='count', show_counts=True)
    upset.plot(fig=fig)  # pass the figure explicitly
    st.pyplot(fig)

    # --- Common to all 4 ---
    common_4 = set.intersection(*millet_sets.values())
    st.markdown("<h5 style='text-align:center;'>Classes Common to All 4 Millets</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame({"BRITE Class": sorted(common_4)}))

    # --- Unique per strain ---
    unique_rows = []
    for strain, classes in millet_sets.items():
        other_classes = set.union(*(c for s, c in millet_sets.items() if s != strain))
        for cls in sorted(classes - other_classes):
            unique_rows.append({"Millet": strain, "BRITE Class": cls})
    st.markdown("<h5 style='text-align:center;'>Unique Classes per Millet</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(unique_rows))

    # --- Common to exactly 3 ---
    common_3_rows = []
    for combo in combinations(millet_sets.keys(), 3):
        s1, s2, s3 = millet_sets[combo[0]], millet_sets[combo[1]], millet_sets[combo[2]]
        common_3 = (s1 & s2 & s3) - common_4
        for cls in sorted(common_3):
            common_3_rows.append({"Millets": " & ".join(combo), "BRITE Class": cls})
    st.markdown("<h5 style='text-align:center;'>Classes Common to Exactly 3 Millets</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(common_3_rows))

    # --- Common to exactly 2 ---
    common_2_rows = []
    for combo in combinations(millet_sets.keys(), 2):
        s1, s2 = millet_sets[combo[0]], millet_sets[combo[1]]
        common_2 = (s1 & s2) - common_4
        # remove common_3 overlaps
        for combo3 in combinations(millet_sets.keys(), 3):
            common_3 = set.intersection(*(millet_sets[c] for c in combo3)) - common_4
            common_2 -= common_3
        for cls in sorted(common_2):
            common_2_rows.append({"Millets": " & ".join(combo), "BRITE Class": cls})
    
    st.markdown("<h5 style='text-align:center;'>Classes Common to Exactly 2 Millets</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(common_2_rows))

#-----------------------------------------------brite subclass--------------------------------------------------

def brsc():

    millet_sets = {}
    for strain, suffix in millet_map.items():
        subclasses = set()
        for prefix in ["ec", "ko"]:
            filename = f"picrust_processed_output_files/{prefix}{suffix}.csv"
            try:
                df = pd.read_csv(filename)
                if "brite_subclass" in df.columns:
                    subclasses.update(df["brite_subclass"].dropna().str.split(";").explode().str.strip())
            except FileNotFoundError:
                st.warning(f"File {filename} not found, skipping.")
        millet_sets[strain] = subclasses

    # UpSet plot
    data = from_memberships(
        [[strain for strain in millet_sets if sc in millet_sets[strain]] for sc in set.union(*millet_sets.values())]
    )
    fig = plt.figure(figsize=(8,6))
    upset = UpSet(data, subset_size='count', show_counts=True)
    upset.plot(fig=fig)  # pass the figure explicitly
    st.pyplot(fig)

    # --- Common to all 4 ---
    common_4 = set.intersection(*millet_sets.values())
    st.markdown("<h5 style='text-align:center;'>Subclasses Common to All 4 Millets</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame({"BRITE Subclass": sorted(common_4)}))

    # --- Unique per strain ---
    unique_rows = []
    for strain, subclasses in millet_sets.items():
        other_subclasses = set.union(*(c for s, c in millet_sets.items() if s != strain))
        for sc in sorted(subclasses - other_subclasses):
            unique_rows.append({"Millet": strain, "BRITE Subclass": sc})
    st.markdown("<h5 style='text-align:center;'>Unique Subclasses per Millet</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(unique_rows))

    # --- Common to exactly 3 ---
    common_3_rows = []
    for combo in combinations(millet_sets.keys(), 3):
        s1, s2, s3 = millet_sets[combo[0]], millet_sets[combo[1]], millet_sets[combo[2]]
        common_3 = (s1 & s2 & s3) - common_4
        for sc in sorted(common_3):
            common_3_rows.append({"Millets": " & ".join(combo), "BRITE Subclass": sc})
    st.markdown("<h5 style='text-align:center;'>Subclasses Common to Exactly 3 Millets</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(common_3_rows))

    # --- Common to exactly 2 ---
    common_2_rows = []
    for combo in combinations(millet_sets.keys(), 2):
        s1, s2 = millet_sets[combo[0]], millet_sets[combo[1]]
        common_2 = (s1 & s2) - common_4
        # remove common_3 overlaps
        for combo3 in combinations(millet_sets.keys(), 3):
            common_3 = set.intersection(*(millet_sets[c] for c in combo3)) - common_4
            common_2 -= common_3
        for sc in sorted(common_2):
            common_2_rows.append({"Millets": " & ".join(combo), "BRITE Subclass": sc})
    st.markdown("<h5 style='text-align:center;'>Subclasses Common to Exactly 2 Millets</h5>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(common_2_rows))

#--------------------------------------------------------------Summary--------------------------------------------------------------------------
def summary():
    with st.sidebar:
        if st.button("Back to Home"):
            go_to("home") 
        with st.sidebar.expander("Summary", expanded=False):
            st.markdown("""
            To be added
            """)
    st.markdown("<h4 style='text-align:center;'>Summary</h4>", unsafe_allow_html=True) 
    st.markdown("hence these millets can be used for probiotics and foof applications")
    
# --------------------------------------------------------------------- Navigation ---------------------------------------------------------------------
page = st.session_state.page
if page == "home":
    home()
elif page == "ec_analysis":
    ec_page()
elif page == "ko_analysis":
    ko_page()
elif page == "pwy_analysis":
    pwy_page()
elif page == "summarized_analysis":
    summary()
elif page == "milletwise_analysis":
    millet()
elif page == "ec_class":
    ec_class()
elif page == "brite":
    brite_class() 
elif page=="trait":
    trait()
elif page=="couq":
    couq()
elif page=="pe":
     pathway_enrichment()
elif page=="cocl":
    cocl(millet_map) 
elif page=="brcl":
    brt()
