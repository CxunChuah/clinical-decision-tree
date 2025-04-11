import streamlit as st

st.set_page_config(page_title="Ankle", layout="wide")
st.sidebar.title("🦶 Ankle")
st.sidebar.info("Use this module to evaluate ankle injuries.")

# Handle theme safely
theme = st.session_state.get("theme", "Pastel Mode")

if theme == "Dark Mode":
    st.markdown(
        """
        <style>
        .appview-container .main {
            background-color: #1e1e1e;
            color: white;
        }
        .block-container {
            background-color: #1e1e1e;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.title("🦶 Ankle Pain Clinical Assessment")
st.write("Begin with a structured pain assessment below.")

# ---------------------- SOCRATES PAIN ASSESSMENT ------------------------
st.header("📋 SOCRATES Pain Assessment")

# Site with conditional "Other"
site_option = st.radio("**S** – Site: Where is the pain located?", ["Lateral", "Medial", "Posterior", "Anterior", "Diffuse", "Other"])
site_other = st.text_input("If other, please specify:") if site_option == "Other" else ""

onset = st.radio("**O** – Onset: When did the pain start?", ["Sudden", "Gradual", "Other"])
character = st.radio("**C** – Character: What does the pain feel like?", ["Sharp", "Dull", "Burning", "Aching", "Throbbing", "Other"])
radiation = st.radio("**R** – Radiation: Does the pain spread anywhere?", ["Yes", "No"])
associated = st.text_input("**A** – Associated symptoms (e.g., swelling, numbness, tingling):")
time = st.radio("**T** – Timing: Is the pain constant or intermittent?", ["Constant", "Intermittent", "Worse in morning", "Worse in evening"])
exacerbating = st.text_input("**E1** – Exacerbating factors: What makes it worse?")
relieving = st.text_input("**E2** – Relieving factors: What makes it better?")

# ---------------------- VAS PAIN SCALE ------------------------
st.subheader("🔢 Severity: Visual Analogue Scale (VAS)")
pain_score = st.radio("Tap to select your pain level:", list(range(0, 11)), horizontal=True)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit — by CxunChuah")
