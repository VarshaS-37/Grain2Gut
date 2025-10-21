import streamlit as st

def millet_page(title, tag):
    st.title(title)
    st.write("### Select which type of analysis you want to explore:")

    # --- CSS for card-style buttons ---
    st.markdown("""
        <style>
        .card-container {
            display: flex;
            justify-content: center;
            gap: 40px;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .stButton>button {
            background-color: #FEF7A2;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            color: #2c3e50;
            font-size: 18px;
            padding: 30px 60px;
            border: none;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #DFFBB9;
            transform: scale(1.05);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }
        </style>
    """, unsafe_allow_html=True)

    # --- Card buttons (centered layout) ---
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        if st.button("🧬 EC Analysis", use_container_width=True):
            go_to(f"{tag}_ec")

    with col2:
        if st.button("🔗 KO Analysis", use_container_width=True):
            go_to(f"{tag}_ko")

    with col3:
        if st.button("🧫 Pathway Analysis", use_container_width=True):
            go_to(f"{tag}_pwy")

    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)

    col_back1, col_back2 = st.columns([1, 1])

    with col_back1:
        if st.button("🔙 Back to Millet Page"):
            go_to(tag)

    with col_back2:
        if st.button("🏠 Back to Home"):
            go_to("home")
