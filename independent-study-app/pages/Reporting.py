import streamlit as st
from datetime import datetime

conn = st.connection("snowflake")

st.subheader("Get Time Summaries :page_facing_up:")

## FUNCTION: Getting the total time spent working
def collect_total_time(times_in, times_out):
    # Define the time format
    time_str_format = "%I:%M %p"

    # Sum the times given
    time = datetime.strptime(times_out[0], time_str_format) - datetime.strptime(times_in[0], time_str_format)
    
    for i in range(1, len(times_in)):
        time += datetime.strptime(times_out[i], time_str_format) - datetime.strptime(times_in[i], time_str_format)

    # Convert the timedelta to hours and minutes
    total_hrs = int(time.total_seconds() // 3600)
    total_mins = int((time.total_seconds() % 3600) // 60)
    
    return total_hrs, total_mins
    
# Get current state of the student information table
ta_logs_df = conn.query("SELECT * FROM INDEP_STUDY.PUBLIC.STUDENT_INFO")

# Rename columns
ta_logs_df.rename(columns = {
    'FIRST_NAME':'First Name', 
    'LAST_NAME':'Last Name',
    'EMAIL':'Email',
    'COURSE':'Course',
    'WORK_DATE':'Date',
    'TIME_IN':'Time In',
    'TIME_OUT':'Time Out',
    'WORK_TYPE':'Work Type'}, inplace = True)

# Get reporting options from user
reporting_option = st.selectbox(
    "Select how to review the time logs:",
    ("View All Logs", "By TA", "By Course", "By Work Type"),
    index = None,
    placeholder = "Select method..."
)

# Reporting Options
if (reporting_option == "View All Logs"): # See everything
    # Show everything
    st.dataframe(ta_logs_df, hide_index = True)

    # Collect total time
    times_in = [time for time in ta_logs_df['Time In']]
    times_out = [time for time in ta_logs_df['Time Out']]
    total_hrs, total_mins = collect_total_time(times_in, times_out)

    # Display
    st.write(f"Total Time Spent Working: **{str(total_hrs)} hours and {str(total_mins)} minutes**")