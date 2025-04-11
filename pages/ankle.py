
import streamlit as st

st.set_page_config(page_title="Ankle Pain", layout="wide")
st.sidebar.title("🦶 Ankle Pain")
st.sidebar.info("Use this module to evaluate ankle injuries.")

# Theme match
theme = st.session_state.get("theme", "Pastel Mode")
page_bg = "#1e1e1e" if theme == "Dark Mode" else "#f0f8ff"
font_color = "#ffffff" if theme == "Dark Mode" else "#000000"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background-color: {page_bg};
        color: {font_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🦶 Ankle Pain Clinical Decision Tree")
st.write("Use this tool to evaluate ankle pain and determine if further imaging or referral is needed.")

# Step 1: Mechanism of Injury
trauma = st.radio("📍 Was there a trauma or twist to the ankle?", ["Yes", "No"])

if trauma == "Yes":
    weight_bearing = st.radio("🦵 Can the person bear weight both immediately and take 4 steps?", ["Yes", "No"])

    st.markdown("### 🩺 Ottawa Ankle Rules")
    malleolar_pain = st.radio("Is there pain in the malleolar zone?", ["Yes", "No"])
    lat_tender = st.radio("Tenderness at posterior edge or tip of lateral malleolus?", ["Yes", "No"])
    med_tender = st.radio("Tenderness at posterior edge or tip of medial malleolus?", ["Yes", "No"])

    st.markdown("### 🚨 Red Flag Screening")
    deformity = st.radio("Is there visible deformity or open wound?", ["Yes", "No"])
    sensation = st.radio("Loss of sensation in the foot or ankle?", ["Yes", "No"])

    if lat_tender == "Yes" or med_tender == "Yes" or weight_bearing == "No":
        st.error("🦴 Suspected fracture — Refer for X-ray (Ottawa Ankle Rules met)")
    elif deformity == "Yes" or sensation == "Yes":
        st.error("🚨 Emergency referral — Possible dislocation or neurovascular compromise")
    else:
        st.success("🟢 Likely sprain — Conservative treatment with RICE and physiotherapy")
else:
    st.info("🔍 No clear trauma — consider overuse, arthritis, referred pain")
    swelling = st.radio("Is there swelling or morning stiffness?", ["Yes", "No"])
    chronicity = st.radio("Has the pain been present for more than 6 weeks?", ["Yes", "No"])

    if chronicity == "Yes":
        st.warning("🧠 Consider chronic causes — possible arthritis or tendinopathy. Refer for assessment.")
    else:
        st.success("🟢 Likely overuse or minor strain — Advise rest and monitor.")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit — by CxunChuah")
