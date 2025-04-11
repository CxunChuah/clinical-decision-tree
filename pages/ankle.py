import streamlit as st

st.set_page_config(page_title="Ankle", layout="wide")
st.sidebar.title("🦶 Ankle")
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
st.write("Answer the following questions and click 'Find out possible conditions' to view results.")

# Step 1: Mechanism
trauma = st.radio("📍 Was there a trauma or twist to the ankle?", ["Yes", "No"], index=None)

# Step 2: Functional
weight_bearing = st.radio("🦵 Can the person bear weight immediately + take 4 steps?", ["Yes", "No"], index=None)

# Step 3: Location of pain
region = st.radio("📌 Where is the primary pain located?", [
    "Lateral (outside)",
    "Medial (inside)",
    "Posterior (Achilles)",
    "Anterior (shin/ankle joint)",
    "Diffuse / General",
], index=None)

# Step 4: Swelling or bruising
swelling = st.radio("💥 Is there swelling or bruising?", ["Yes", "No"], index=None)

# Step 5: Red flags
red_flag = st.radio("🚨 Are there any of the following? (open wound, deformity, loss of sensation)", ["Yes", "No"], index=None)

# Trigger logic only on button click
if st.button("Find out possible conditions"):
    st.markdown("---")

    if red_flag == "Yes":
        st.error("🚨 Emergency concern — refer for imaging & urgent care.")

    elif trauma == "Yes":
        if weight_bearing == "No" or (region in ["Lateral (outside)", "Medial (inside)"] and swelling == "Yes"):
            st.warning("🦴 Possible fracture — Ottawa rules suggest X-ray.")
        elif region == "Lateral (outside)":
            st.info("🔹 Likely lateral ligament sprain (ATFL, CFL). Conservative management.")
        elif region == "Medial (inside)":
            st.info("🔹 Possible deltoid ligament strain or avulsion fracture.")
        elif region == "Posterior (Achilles)":
            st.warning("⚠️ Possible Achilles strain or rupture — perform Thompson test.")
        elif region == "Anterior (shin/ankle joint)":
            st.info("🔹 May be anterior impingement or joint capsule irritation.")
        else:
            st.info("🩺 Could be mixed soft tissue injury — monitor & treat conservatively.")

    elif trauma == "No":
        if region == "Posterior (Achilles)":
            st.info("🔹 Possible Achilles tendinopathy — often overuse-related.")
        elif region == "Lateral (outside)":
            st.info("🔹 Peroneal tendon strain or instability suspected.")
        elif region == "Medial (inside)":
            st.info("🔹 Consider tibialis posterior tendinopathy or tarsal tunnel syndrome.")
        elif region == "Anterior (shin/ankle joint)":
            st.info("🔹 Shin splints, anterior impingement, or arthritis possible.")
        else:
            st.info("🔍 Consider arthritis, referred pain, or general overuse.")

    else:
        st.warning("⚠️ Please answer all questions before proceeding.")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit — by CxunChuah")
