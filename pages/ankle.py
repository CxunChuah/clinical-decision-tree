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

site = st.text_input("**S** – Site: Where is the pain located?")
onset = st.text_input("**O** – Onset: When did the pain start? Was it sudden or gradual?")
character = st.text_input("**C** – Character: What does the pain feel like? (e.g., sharp, dull, burning)")
radiation = st.text_input("**R** – Radiation: Does the pain spread anywhere?")
associated = st.text_input("**A** – Associated symptoms: Any swelling, numbness, tingling?")
time = st.text_input("**T** – Timing: Constant or intermittent? Worse at certain times?")
exacerbate_relievers = st.text_input("**E** – Exacerbating/Relieving factors: What makes it better or worse?")

# ---------------------- VAS PAIN SCALE ------------------------
st.subheader("🔢 Severity: Visual Analogue Scale (VAS)")
pain_score = st.slider("Rate your current pain level:", 0, 10, step=1)

# ---------------------- SUBMIT BUTTON ------------------------
if st.button("🧾 Submit Pain Profile"):
    st.markdown("---")
    st.subheader("🧠 Summary of Pain Assessment")
    st.markdown(f"**Site:** {site}")
    st.markdown(f"**Onset:** {onset}")
    st.markdown(f"**Character:** {character}")
    st.markdown(f"**Radiation:** {radiation}")
    st.markdown(f"**Associated symptoms:** {associated}")
    st.markdown(f"**Timing:** {time}")
    st.markdown(f"**Exacerbating/Relieving Factors:** {exacerbate_relievers}")
    st.markdown(f"**VAS Score:** {pain_score}/10")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit — by CxunChuah")
