# Import python packages
import streamlit as st

# Define App Title, shared between pages
st.title("Wolftime 2.0 :clock1:")

# Information on how to use the app (unique to the homepage)
def homepage():
    st.write("Welcome to Wolftime 2.0!")
    st.markdown("Navigate to the **Log Hours** page to log your work hours and details.")
    st.markdown("Navigate to the **Generate Reports** page to look at the existing information regarding work hours.")

# Set up page navigation
pg = st.navigation([
    st.Page(homepage, title = "Homepage"),
    st.Page("pages/Clocking.py", title = "Log Hours"),
    st.Page("pages/Reporting.py", title = "Generate Reports"),
], position = "top")

pg.run()