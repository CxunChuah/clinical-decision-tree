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
        <div style='background:{color}; padding:10px; border-radius:10px; width:{pain_score*10}%; color:white; text-align:center;'>
            Pain Level: {pain_score}/10
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------- OBSERVATION + PALPATION ------------------------
st.header("🧐 Observation")
observation_general = st.multiselect("General observation findings:", [
    "Antalgic gait",
    "Altered posture",
    "Guarding behavior",
    "Use of assistive device"
])

observation_local = st.multiselect("Local signs at ankle:", [
    "Swelling",
    "Bruising",
    "Redness",
    "Deformity",
    "Muscle wasting"
])

st.header("🤲 Palpation")
palpation_sites = st.multiselect("Tenderness on palpation:", [
    "ATFL (anterior talofibular ligament)",
    "CFL (calcaneofibular ligament)",
    "Deltoid ligament",
    "Medial malleolus",
    "Lateral malleolus",
    "Achilles tendon",
    "Plantar fascia",
    "Sinus tarsi",
    "Navicular / base of 5th MT"
])

st.markdown("---")
st.caption("Built with ❤️ using Streamlit — by CxunChuah")
