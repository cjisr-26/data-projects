# Import python packages
import streamlit as st
import re
from datetime import datetime

conn = st.connection("snowflake")

st.subheader("Log Your Hours :writing_hand:")
    
## Error-Checking function: Valid time strings
def valid_times(time_in_str, time_out_str):
    time_str_format = "%I:%M %p"

    # Check if time in is less than time out
    # Catch error if either time does not match the correct format
    try:
        if (datetime.strptime(time_in_str, time_str_format) < datetime.strptime(time_out_str, time_str_format)):
            return True
        else:
            return False
    except ValueError:
        return False
        
# Get user input
fname = st.text_input("Enter First Name")
lname = st.text_input("Enter Last Name")
email = st.text_input("Enter Email (must end with \'@ncsu.edu\')")
course = st.text_input("Enter Course Code", placeholder = "i.e., CSC101, E102")
date = st.date_input("Enter Date", format = "MM/DD/YYYY")
time_in = st.text_input("Enter Time In", placeholder = "HH:MM AM/PM")
time_out = st.text_input("Enter Time Out", placeholder = "HH:MM AM/PM")
work_type = st.selectbox("Enter Work Type",
    ("Office Hours", "Grading", "Proctoring", "Lab", "Communication", "Meeting"),
    index = None,
    placeholder = "Select work type...")

# Submit input
submit_btn = st.button("Submit", type = "primary")

if (submit_btn):
    # Error Checking- No blanks, valid email, valid course code, valid timeframe
    if (not fname.strip() or not lname.strip() or not email.strip() or not course.strip() or date == "" or
        not time_in.strip() or not time_out.strip() or work_type == None):
        st.error("Please Provide Values for All Fields")  
    elif (not email.endswith("@ncsu.edu") or email.count("@") != 1):
        st.error("Please Enter a Valid Email")
    elif (not bool(re.fullmatch(r'[A-Za-z]{1,3}\d{3}', course))):
        st.error("Please Enter a Valid Course Code")
    elif (not valid_times(time_in, time_out)):
        st.error("Please Enter Valid Time(s)")
    else:
        # Use a parameterized query to insert --> more secure
        insert_stmnt = "INSERT INTO INDEP_STUDY.PUBLIC.STUDENT_INFO \
                        (FIRST_NAME, LAST_NAME, EMAIL, COURSE, WORK_DATE, TIME_IN, TIME_OUT, WORK_TYPE)\
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
        params = [fname, lname, email, course, date, time_in, time_out, work_type]
        
        try:
            with conn.cursor() as cursor:
                cursor.execute(insert_stmnt, params)
                
            st.success("Submission Success!")
        except Exception as e:
            st.error("Submission Error")
            st.error(e)