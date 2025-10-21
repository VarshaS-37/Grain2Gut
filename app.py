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
        if st.button("Proso Millet\nEnterococcus casseliflavus\nPP355677"):
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
    if st.button("Back to Home"):
        go_to("home")


"""def ec_page(title, tag):
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
            go_to("home")"""

def ec_page(title, tag):
    st.title(f"{title} - EC Analysis")
    suffix = tag_to_suffix.get(tag, "")

    try:
        df = pd.read_csv(f"ec{suffix}.csv")

        # Assuming first column is EC number
        st.write("Click on an EC number to view its summary:")

        # Display table with ECs as clickable links
        for index, row in df.iterrows():
            ec_number = str(row.iloc[0])  # First column = EC number
            cols = st.columns(len(row))
            for i, val in enumerate(row):
                if i == 0:
                    if cols[i].button(f"{ec_number}", key=f"{tag}_ec_{ec_number}"):
                        st.session_state.selected_ec = ec_number
                        st.session_state.back_page = f"{tag}_ec"
                        go_to("ec_detail")
                else:
                    cols[i].write(val)

    except FileNotFoundError:
        st.error(f"File ec{suffix}.csv not found.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back to Millet Page"):
            go_to(tag)
    with col2:
        if st.button("Back to Home"):
            go_to("home")
def ec_detail_page():
    ec_number = st.session_state.get("selected_ec", None)

    if ec_number is None:
        st.error("No EC number selected.")
        return

    st.title(f"EC Detail: {ec_number}")

    # Sample static summary — replace with dynamic logic or dictionary
    ec_summaries = {
        "1.1.1.1": "Alcohol dehydrogenase — converts alcohols to aldehydes.",
        "2.7.1.1": "Hexokinase — catalyzes glucose to glucose-6-phosphate.",
        # Add more EC summaries as needed
    }

    summary = ec_summaries.get(ec_number, "No summary available for this EC number.")
    st.markdown(f"### Summary\n{summary}")

    st.markdown("---")
    st.markdown(f"**External Link**: [KEGG EC {ec_number}](https://www.genome.jp/dbget-bin/www_bget?ec:{ec_number})")

    if st.button("Back"):
        go_to(st.session_state.get("back_page", "home"))

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
elif page == "ec_detail":
    ec_detail_page()
