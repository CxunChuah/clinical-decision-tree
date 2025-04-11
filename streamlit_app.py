
import streamlit as st

st.set_page_config(page_title="Clinical Decision Tree", layout="wide")

# Theme selector
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Medical_icon.png/240px-Medical_icon.png", width=120)
st.sidebar.title("🩺 Clinical Decision Tree")
st.sidebar.markdown("---")
mode = st.sidebar.radio("🎨 Select a Theme", ["Pastel Mode", "Dark Mode"])
st.session_state.theme = mode

# Apply theme colors
if mode == "Dark Mode":
    page_bg = "#1e1e1e"
    font_color = "#ffffff"
else:
    page_bg = "#f0f8ff"  # pastel blue
    font_color = "#000000"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background-color: {page_bg};
        color: {font_color};
    }}
    .sidebar .sidebar-content {{
        background-color: #ffffff;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧍‍♂️ Clinical Decision Tree Hub")
st.markdown("Welcome to your clinical triage tool. Use the sidebar to explore region-specific tools.")

st.success("Currently available: Ankle Pain Assessment (under 'Pages' menu on the left)")

st.markdown("---")
st.caption("Built with ❤️ by CxunChuah")
