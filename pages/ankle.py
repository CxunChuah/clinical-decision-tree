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

# App title
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
    "
