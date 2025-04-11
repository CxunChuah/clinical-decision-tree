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
pain_score = st.radio("Rate your current pain level (0 = no pain, 10 = worst possible):",
                      options=list(range(0, 11)),
                      horizontal=True,
                      index=None)

if pain_score is not None:
    color = "#00cc66" if pain_score <= 3 else "#ffaa00" if pain_score <= 6 else "#ff3333"
    st.markdown(
        f"""
        <div style='border: 1px solid #ddd; border-radius: 10px; overflow: hidden; width: 100%; height: 25px; background-color: #eee;'>
            <div style='height: 100%; width: {pain_score * 10}%; background-color: {color}; text-align: center; color: white;'>
                {pain_score}/10
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------- OBSERVATION ------------------------
st.header("🧐 Observation")

st.subheader("Part A – Gait Pattern")
gait_pattern = st.selectbox("Observed gait type:", ["Normal", "Antalgic", "High-steppage", "Trendelenburg", "Limp", "Other"])

st.subheader("Part B – Consciousness Level")
consciousness = st.radio("Patient's consciousness level:", ["Alert", "Drowsy", "Confused", "Unresponsive"])

st.subheader("Local Observation Findings")
cols = st.columns(3)
local_signs = {}
options = ["Swelling", "Bruising", "Redness", "Deformity", "Muscle wasting"]
for i, opt in enumerate(options):
    with cols[i % 3]:
        local_signs[opt] = st.checkbox(opt)

# ---------------------- PALPATION PLACEHOLDER ------------------------
st.header("🤲 Palpation")
st.info("Palpation section will be enhanced next.")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit — by CxunChuah")
