# Detect theme selected on main page
theme = st.session_state.get("theme", "Pastel Mode")

# Apply dark mode CSS override if selected
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
