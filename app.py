def millet_page(title, tag):
    st.title(title)
    st.write("Select which type of analysis you want to explore:")

    # --- CSS for card-style buttons ---
    st.markdown("""
        <style>
        .analysis-grid {
            display: flex;
            justify-content: center;
            gap: 60px;
            flex-wrap: wrap;
            margin-top: 30px;
        }
        .card {
            background-color: #FEF7A2;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            padding: 30px 50px;
            width: 250px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .card:hover {
            background-color: #DFFBB9;
            transform: scale(1.05);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }
        .card h3 {
            color: #2c3e50;
            font-size: 22px;
            margin-top: 15px;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- Card layout ---
    st.markdown("""
        <div class="analysis-grid">
            <div class="card" onclick="window.location.href='?nav=ec'">
                <div style="font-size:40px;">🧬</div>
                <h3>EC Analysis</h3>
            </div>
            <div class="card" onclick="window.location.href='?nav=ko'">
                <div style="font-size:40px;">🔗</div>
                <h3>KO Analysis</h3>
            </div>
            <div class="card" onclick="window.location.href='?nav=pwy'">
                <div style="font-size:40px;">🧫</div>
                <h3>Pathway Analysis</h3>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- JavaScript event handling for navigation ---
    nav = st.query_params.get("nav", [""])[0]

    if nav == "ec":
        go_to(f"{tag}_ec")
    elif nav == "ko":
        go_to(f"{tag}_ko")
    elif nav == "pwy":
        go_to(f"{tag}_pwy")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🏠 Back to Home"):
        go_to("home")

