import streamlit as st
#from datetime import datetime

conn = st.connection("snowflake")

st.subheader("Get Time Summaries :page_facing_up:")

# Get current state of the student information table
ta_logs_df = conn.query("SELECT * FROM INDEP_STUDY.PUBLIC.STUDENT_INFO")

st.dataframe(ta_logs_df, hide_index = True)