import streamlit as st
from datetime import datetime

# Create Snowflake connection and session for data retrieval
conn = st.connection("snowflake")
session = conn.session()

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
# Get current state of the student information table
ta_logs = session.sql("SELECT * FROM INDEP_STUDY.PUBLIC.STUDENT_INFO")

# Convert sql table to a pandas dataframe
ta_logs_df = ta_logs.to_pandas()
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
elif (reporting_option == "By TA"): # See select TAs
    # Get the first and last names of the TAs to select
    ta_names = []

    for i in range(ta_logs_df['First Name'].nunique()):
        ta_names.append(
            ta_logs_df['First Name'].unique()[i] + " " + ta_logs_df['Last Name'].unique()[i])

    # Get the user selection
    ta_options = st.multiselect(
        "Select the TAs to view.",
        ta_names
    )

    # When the user makes a selection, filter the table, and display the user's selection
    if (ta_options):
        options_first = []
        options_last = []

        for i in range(len(ta_options)):
            options_first.append(ta_options[i].split()[0])
            options_last.append(ta_options[i].split()[1])

        ta_logs_filt_df = ta_logs_df.loc[ta_logs_df['First Name'].isin(options_first) & ta_logs_df['Last Name'].isin(options_last)]
        st.dataframe(ta_logs_filt_df, hide_index = True)

        # Collect total time
        times_in = [time for time in ta_logs_filt_df['Time In']]
        times_out = [time for time in ta_logs_filt_df['Time Out']]
        total_hrs, total_mins = collect_total_time(times_in, times_out)

        # Display
        st.write(f"Total Time Spent Working for Selected TA(s): **{str(total_hrs)} hours and {str(total_mins)} minutes**")
    
elif (reporting_option == "By Course"): # See select courses
    # Get the courses available
    course_names = ta_logs_df['Course'].unique()
    
    # Get the user selection
    course_options = st.multiselect(
        "Select the Courses to view.",
        course_names
    )
    
    # When the user makes a selection, filter the table, and display the user's selection
    if (course_options): 
        ta_logs_filt_df = ta_logs_df.loc[ta_logs_df['Course'].isin(course_options)]
        st.dataframe(ta_logs_filt_df, hide_index = True)

        # Collect total time
        times_in = [time for time in ta_logs_filt_df['Time In']]
        times_out = [time for time in ta_logs_filt_df['Time Out']]
        total_hrs, total_mins = collect_total_time(times_in, times_out)

        # Display
        st.write(f"Total Time Spent Working for Selected Course(s): **{str(total_hrs)} hours and {str(total_mins)} minutes**")
        
elif (reporting_option == "By Work Type"): # See select reporting options
    # Get the work types available
    work_names = ta_logs_df['Work Type'].unique()

    # Get the user selection
    work_options = st.multiselect(
        "Select the Work Types to view.",
        work_names
    )

    # When the user makes a selection, filter the table, and display the user's selection
    if (work_options): 
        ta_logs_filt_df = ta_logs_df.loc[ta_logs_df['Work Type'].isin(work_options)]
        st.dataframe(ta_logs_filt_df, hide_index = True)

        # Collect total time
        times_in = [time for time in ta_logs_filt_df['Time In']]
        times_out = [time for time in ta_logs_filt_df['Time Out']]
        total_hrs, total_mins = collect_total_time(times_in, times_out)

        # Display
        st.write(f"Total Time Spent Working for Selected Work Type(s): **{str(total_hrs)} hours and {str(total_mins)} minutes**")



    